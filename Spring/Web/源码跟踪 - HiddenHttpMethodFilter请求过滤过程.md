# 源码跟踪[1] - HiddenHttpMethodFilter的请求过滤过程

## 场景描述
现在的请求设计都在使用RESTful风格, 即通过 **HTTP动词**(GET POST DELETE PUT PATCH) 和 **URI**(统一资源定位符).  

但是浏览器上的`<form>`只能发出`POST`和`GET`请求, 所以为了处理带有其他的HTTP动词的RESTful请求, 所以一种规范就是将普通的`post`请求带上一个隐藏参数(不被用户所看到), 来用这种方式告诉服务端这其实是一个`PUT`或者`DELETE`请求.

对于Spring, 它就提供了一个 filter 来增强带有隐藏参数的`POST`请求, 定义在`org.springframework.web.filter.HiddenHttpMethodFilter.java`

## 单步跟踪
分析一个典型的`<form>`表单的提交的`PUT`或`DELETE`请求被`HiddenHttpMethodFilter`捕捉并处理的过程

1. 一个最常见的`HttpServletRequest request` 进入 `HiddenHttpMethodFilter` 的 `doFilterInternal()` 方法.
2. 如果请求方法是`POST` 那么, 去尝试取`String paramValue`, 如果它不是空, 并且是`ALLOWED_METHODS`中的一个, 那么就将它转化成大写的`String method`, 然后和`HttpServletRequest request`一起送入 `HttpMethodRequestWrapper`
3. `HttpMethodRequestWrapper`将其`method`设置为`POST PUT DELETE`

#### 源码 `org.springframework.web.filter.HiddenHttpMethodFilter.java`
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
Spring把所有请求分成两类, **GET请求**和**非GET请求**, 对于后者采用了统一的办法就是进行了包装, 这样无论从网页端发过来的类似`POST {_method="PUT"}`的"伪POST"请求, 还是本身就是纯POST请求, 都可以通过这个包装器来统一成**RESTful**风格.



