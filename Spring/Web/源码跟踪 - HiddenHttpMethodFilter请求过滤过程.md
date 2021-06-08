## 场景描述
现在的请求设计都在使用RESTful风格, 即通过 **HTTP动词**(GET POST DELETE PUT PATCH) 和 **URI**(统一资源定位符).  

但是浏览器上只能发出`POST`和`GET`请求, 所以为了处理带有其他的HTTP动词的RESTful请求, 所以一种规范就是将普通的`post`请求带上一个隐藏参数(不被用户所看到), 来用这种方式告诉服务端这其实是一个`PUT`或者`DELETE`请求.

对于Spring, 它就提供了一个 filter 来增强带有隐藏参数的`POST`请求, 定义在`org.springframework.web.filter.HiddenHttpMethodFilter.java`

## 源码跟踪
分析一个典型的`<form>`表单提交后被`HiddenHttpMethodFilter`捕捉并处理的过程

#### 源码
`org.springframework.web.filter.HiddenHttpMethodFilter.java`
```java
public class HiddenHttpMethodFilter extends OncePerRequestFilter {

	private static final List<String> ALLOWED_METHODS =
			Collections.unmodifiableList(Arrays.asList(HttpMethod.PUT.name(),
					HttpMethod.DELETE.name(), HttpMethod.PATCH.name()));

	/** Default method parameter: {@code _method}. */
	public static final String DEFAULT_METHOD_PARAM = "_method";

	private String methodParam = DEFAULT_METHOD_PARAM;


	/**
	 * Set the parameter name to look for HTTP methods.
	 * @see #DEFAULT_METHOD_PARAM
	 */
	public void setMethodParam(String methodParam) {
		Assert.hasText(methodParam, "'methodParam' must not be empty");
		this.methodParam = methodParam;
	}

	@Override
	protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
			throws ServletException, IOException {

		HttpServletRequest requestToUse = request;

		if ("POST".equals(request.getMethod()) && request.getAttribute(WebUtils.ERROR_EXCEPTION_ATTRIBUTE) == null) {
			String paramValue = request.getParameter(this.methodParam);
			if (StringUtils.hasLength(paramValue)) {
				String method = paramValue.toUpperCase(Locale.ENGLISH);
				if (ALLOWED_METHODS.contains(method)) {
					requestToUse = new HttpMethodRequestWrapper(request, method);
				}
			}
		}

		filterChain.doFilter(requestToUse, response);
	}


	/**
	 * Simple {@link HttpServletRequest} wrapper that returns the supplied method for
	 * {@link HttpServletRequest#getMethod()}.
	 */
	private static class HttpMethodRequestWrapper extends HttpServletRequestWrapper {

		private final String method;

		public HttpMethodRequestWrapper(HttpServletRequest request, String method) {
			super(request);
			this.method = method;
		}

		@Override
		public String getMethod() {
			return this.method;
		}
	}

}
```
## 小结
## 拓展

*来源于网络Spring教程*

