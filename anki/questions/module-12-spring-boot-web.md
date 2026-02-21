## Question

What is a web server?<br><br>

Please select 1 option<br><br>

A) A database that stores web pages<br>
B) A program that listens for HTTP requests and responds with data<br>
C) A browser plugin that renders HTML<br>
D) A protocol for transferring files

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>WEB SERVER:</strong> A server is a program (or machine) that:<br>
• <strong>Waits</strong> for requests<br>
• <strong>Responds</strong> to requests<br><br>

A web server specifically:<br>
• Listens to <strong>HTTP requests</strong><br>
• Responds with <strong>data</strong> (HTML, JSON, etc.)<br><br>

<strong>A) is incorrect:</strong> A database stores data, not HTTP requests.<br>
<strong>C) is incorrect:</strong> Browsers render HTML — they are clients, not servers.<br>
<strong>D) is incorrect:</strong> HTTP is the protocol; a server is the program that uses it.

## Question

What does HTTP stand for, and what does it define?<br><br>

Please select 2 options<br><br>

A) HTTP = HyperText Transfer Protocol<br>
B) HTTP = HyperText Transaction Process<br>
C) HTTP defines how to send a request and structure a response<br>
D) HTTP defines the database schema for web applications<br>
E) HTTP defines methods like GET, POST, PUT, DELETE

## Réponse

<strong>Réponse correcte :</strong> A) et C) et E) — mais si 2 options attendues : <strong>A) et C)</strong><br><br>

<strong>HTTP = HyperText Transfer Protocol</strong><br><br>

It defines:<br>
• <strong>How to send a request</strong><br>
• <strong>How to structure a response</strong><br>
• <strong>Methods</strong>: GET, POST, PUT, DELETE…<br>
• <strong>Status codes</strong>: 200, 404, 500…<br><br>

HTTP is the <strong>language of the web</strong> — the means of communication between client and server.<br><br>

<strong>B) is incorrect:</strong> The full form is HyperText <em>Transfer</em> Protocol.<br>
<strong>D) is incorrect:</strong> HTTP has nothing to do with database schemas.

## Question

Match each HTTP method to its correct operation.<br><br>

Please select 1 option<br><br>

A) GET = create, POST = read, PUT = delete, DELETE = modify<br>
B) GET = read, POST = create, PUT = modify, DELETE = delete<br>
C) GET = delete, POST = modify, PUT = read, DELETE = create<br>
D) GET = read, POST = modify, PUT = create, DELETE = delete

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>HTTP METHODS:</strong><br>
• <strong>GET</strong> → Read / retrieve data<br>
• <strong>POST</strong> → Create a new resource<br>
• <strong>PUT</strong> → Update / modify an existing resource<br>
• <strong>DELETE</strong> → Remove a resource<br><br>

Memory tip: <strong>CRUD</strong> = Create / Read / Update / Delete → POST / GET / PUT / DELETE<br><br>

<strong>A), C), D) are incorrect:</strong> All mix up the correct mappings.

## Question

Which HTTP status codes are correctly matched to their meaning?<br><br>

Please select 3 options<br><br>

A) 200 → OK<br>
B) 201 → Not Found<br>
C) 404 → Not Found<br>
D) 500 → Server Error<br>
E) 401 → Created

## Réponse

<strong>Réponse correcte :</strong> A), C), D)<br><br>

<strong>KEY STATUS CODES:</strong><br>
• <strong>200</strong> → OK (request succeeded)<br>
• <strong>201</strong> → Created (resource created successfully)<br>
• <strong>400</strong> → Bad Request (client error)<br>
• <strong>401</strong> → Unauthorized (authentication required)<br>
• <strong>404</strong> → Not Found<br>
• <strong>500</strong> → Internal Server Error<br><br>

<strong>B) is incorrect:</strong> 201 = Created, not Not Found.<br>
<strong>E) is incorrect:</strong> 401 = Unauthorized, not Created.

## Question

What is the role of a port in a web application?<br><br>

Please select 1 option<br><br>

A) It encrypts the HTTP traffic between client and server<br>
B) It identifies which service to connect to on a machine<br>
C) It stores the IP address of the server<br>
D) It defines the HTTP method used in the request

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>PORT:</strong> A number that identifies a specific service on a machine.<br><br>

Example:<br>

```
http://localhost:8080
```

• <strong>localhost</strong> → your own computer (127.0.0.1)<br>
• <strong>8080</strong> → the port number<br>
• <strong>http</strong> → the protocol<br><br>

Without a port, the browser doesn't know which service to talk to on the machine.<br><br>

<strong>A) is incorrect:</strong> Encryption is handled by HTTPS / TLS, not the port.<br>
<strong>C) is incorrect:</strong> The IP address identifies the machine; the port identifies the service.<br>
<strong>D) is incorrect:</strong> HTTP methods (GET, POST…) are part of the request, not the port.

## Question

What does API stand for, and what does it define?<br><br>

Please select 1 option<br><br>

A) Application Protocol Interface — it defines the transport layer<br>
B) Application Programming Interface — it defines the functionalities an application exposes<br>
C) Automated Processing Interface — it defines how databases are queried<br>
D) Application Programming Interface — it defines the HTTP protocol

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>API = Application Programming Interface</strong><br><br>

It defines:<br>
• The <strong>routes</strong> (e.g. <code>/users</code>)<br>
• The <strong>available actions</strong> (what you can do)<br>
• The <strong>data sent</strong> and <strong>data received</strong><br><br>

Think of it as: <strong>API = what the application allows you to do</strong>.<br><br>

<strong>A) is incorrect:</strong> The full form is correct but the definition is wrong — APIs don't define transport.<br>
<strong>C) is incorrect:</strong> APIs are not about database queries.<br>
<strong>D) is incorrect:</strong> HTTP is a protocol; the API uses HTTP but doesn't define it.

## Question

What is the correct distinction between HTTP and an API?<br><br>

Please select 1 option<br><br>

A) HTTP and API are the same thing — both define routes and transport<br>
B) HTTP is the protocol (how we communicate), API is the interface (what is available)<br>
C) API is the protocol, HTTP is the interface<br>
D) HTTP defines the routes; API defines the transport

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>HTTP vs API:</strong><br><br>

| | HTTP | API |
| --- | --- | --- |
| Type | Protocol | Interface |
| Role | How we communicate | What is available |
| Analogy | The road | The shop<br><br>

• <strong>HTTP</strong> = the road (means of transport)<br>
• <strong>API</strong> = the shop (what you can do/access)<br><br>

<strong>A) is incorrect:</strong> They are distinct concepts.<br>
<strong>C) is incorrect:</strong> The roles are reversed.<br>
<strong>D) is incorrect:</strong> HTTP doesn't define routes — the API does.

## Question

What is REST?<br><br>

Please select 1 option<br><br>

A) A database query language<br>
B) An architectural style that organizes how HTTP is used in APIs<br>
C) A Java framework that replaces Spring Boot<br>
D) A replacement for HTTP

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>REST = Representational State Transfer</strong><br><br>

REST is an <strong>architectural style</strong> (not a protocol, not a framework).<br><br>

REST says:<br>
• Use <strong>HTTP properly</strong><br>
• <strong>GET</strong> to read<br>
• <strong>POST</strong> to create<br>
• <strong>PUT</strong> to update<br>
• <strong>DELETE</strong> to delete<br><br>

REST <strong>organizes</strong> the API — it gives structure to how HTTP is used.<br><br>

<strong>A) is incorrect:</strong> SQL is a query language; REST has nothing to do with databases directly.<br>
<strong>C) is incorrect:</strong> REST is a style, not a framework.<br>
<strong>D) is incorrect:</strong> REST uses HTTP — it doesn't replace it.

## Question

What is the key difference between a console application and a server application?<br><br>

Please select 1 option<br><br>

A) A console app listens on a port and responds to HTTP requests<br>
B) A server app runs only in a terminal with no external connections<br>
C) A console app runs in the terminal only; a server app listens on a port and responds to HTTP requests<br>
D) Both are equivalent — Java SE handles HTTP by default

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Console application:</strong><br>

```java
System.out.println("Hello");
```

• No port<br>
• No HTTP<br>
• No requests<br>
• Terminal only<br><br>

<strong>Server application:</strong><br>
• Listens on a <strong>port</strong><br>
• Waits for <strong>HTTP requests</strong><br>
• Responds to a <strong>browser or client</strong><br><br>

<strong>A) is incorrect:</strong> It's the server app, not the console app, that listens on a port.<br>
<strong>B) is incorrect:</strong> A server app is not terminal-only.<br>
<strong>D) is incorrect:</strong> Plain Java SE cannot handle HTTP without a framework.

## Question

Can a plain Java SE application (no framework, no library) respond to HTTP requests from a browser?<br><br>

Please select 1 option<br><br>

A) Yes — Java SE includes an embedded HTTP server by default<br>
B) No — a framework like Spring Boot or Helidon is required to handle HTTP<br>
C) Yes — but only for GET requests<br>
D) Yes — using System.out to write HTTP responses

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

A <strong>plain Java SE application</strong> cannot respond to a browser on its own.<br><br>

To handle HTTP, you need a framework or library that:<br>
• <strong>Starts an embedded server</strong><br>
• <strong>Binds to a port</strong><br>
• <strong>Handles request parsing and response writing</strong><br><br>

Examples:<br>
• <strong>Spring Boot</strong> → embeds Tomcat<br>
• <strong>Helidon</strong> → lightweight HTTP server<br><br>

<strong>A) is incorrect:</strong> Java SE has no embedded HTTP server out of the box.<br>
<strong>C) is incorrect:</strong> No HTTP method is supported without a framework.<br>
<strong>D) is incorrect:</strong> System.out writes to the terminal, not to HTTP responses.

## Question

What does Helidon add to a Java SE application?<br><br>

Please select 1 option<br><br>

A) A GUI interface for desktop apps<br>
B) A mini embedded HTTP server, enabling the app to receive web requests<br>
C) A full dependency injection container like Spring<br>
D) Direct database access without JDBC

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Helidon:</strong><br>
• Lightweight Java framework<br>
• Adds a <strong>mini embedded HTTP server</strong><br>
• Transforms a console Java SE app into a <strong>web server</strong><br><br>

```
Console app  →  [Helidon]  →  Web server
```

It handles:<br>
• Listening on a <strong>port</strong><br>
• Receiving <strong>HTTP requests</strong><br>
• Sending <strong>HTTP responses</strong><br><br>

<strong>A) is incorrect:</strong> Helidon is for web/server, not GUI.<br>
<strong>C) is incorrect:</strong> Helidon is lightweight — full DI is more Spring's territory.<br>
<strong>D) is incorrect:</strong> Database access is unrelated to what Helidon provides.

## Question

What does Spring Boot provide compared to a plain Java SE app?<br><br>

Please select 2 options<br><br>

A) It starts an embedded Tomcat server automatically<br>
B) It compiles Java faster than the standard JDK<br>
C) It exposes REST endpoints via annotations like @GetMapping<br>
D) It replaces the JVM with its own runtime<br>
E) It forces you to use XML configuration files

## Réponse

<strong>Réponse correcte :</strong> A) et C)<br><br>

<strong>Spring Boot:</strong><br>
• <strong>Starts an embedded Tomcat server</strong> automatically (no external server needed)<br>
• <strong>Exposes REST endpoints</strong> via annotations<br>
• <strong>Manages HTTP automatically</strong><br><br>

Example annotation:<br>

```java
@GetMapping("/users")
public List<User> getUsers() {
    return userService.findAll();
}
```

<strong>B) is incorrect:</strong> Spring Boot does not speed up compilation.<br>
<strong>D) is incorrect:</strong> Spring Boot runs on the standard JVM.<br>
<strong>E) is incorrect:</strong> Spring Boot defaults to <em>no XML</em> — it uses annotations and auto-configuration.

## Question

Which Spring Boot annotation maps a method to an HTTP GET request on the route <code>/products</code>?<br><br>

Please select 1 option<br><br>

A) <code>@HttpGet("/products")</code><br>
B) <code>@RequestMapping(method = "GET")</code> only<br>
C) <code>@GetMapping("/products")</code><br>
D) <code>@RestController("/products")</code>

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

```java
@GetMapping("/products")
public List<Product> getProducts() {
    return productService.findAll();
}
```

<strong>Common Spring Boot HTTP annotations:</strong><br>
• <strong>@GetMapping</strong> → HTTP GET<br>
• <strong>@PostMapping</strong> → HTTP POST<br>
• <strong>@PutMapping</strong> → HTTP PUT<br>
• <strong>@DeleteMapping</strong> → HTTP DELETE<br><br>

<strong>A) is incorrect:</strong> <code>@HttpGet</code> doesn't exist in Spring.<br>
<strong>B) is incorrect:</strong> <code>@RequestMapping</code> works but <code>@GetMapping</code> is the idiomatic shortcut.<br>
<strong>D) is incorrect:</strong> <code>@RestController</code> marks the class, not a specific route.

## Question

What is the correct order of a modern web request/response cycle?<br><br>

Please select 1 option<br><br>

A) Database → Business logic → API → Server → HTTP Response → Browser<br>
B) Browser → HTTP Request → Spring Server → REST API → Business logic → Database → HTTP Response<br>
C) Browser → Database → HTTP Request → Spring Server → HTTP Response<br>
D) HTTP Request → Browser → Spring Server → Database → REST API

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>Modern web architecture flow:</strong><br>

```
Browser (client)
      ↓  HTTP Request
Spring Server
      ↓
  REST API
      ↓
Business Logic
      ↓
  Database
      ↓  HTTP Response
Browser (client)
```

Each layer has a clear responsibility:<br>
• <strong>Browser</strong> → sends the request, displays the response<br>
• <strong>Spring Server</strong> → receives and routes the request<br>
• <strong>REST API</strong> → defines available endpoints<br>
• <strong>Business Logic</strong> → processes data<br>
• <strong>Database</strong> → stores/retrieves data<br><br>

<strong>A), C), D) are incorrect:</strong> They all present the layers in the wrong order.

## Question

What HTTP status code should a REST API return when a new resource is successfully created?<br><br>

Please select 1 option<br><br>

A) 200<br>
B) 204<br>
C) 201<br>
D) 200 or 201 — both are equivalent

## Réponse

<strong>Réponse correcte :</strong> C)<br><br>

<strong>Status codes for success:</strong><br>
• <strong>200 OK</strong> → General success (typically for GET)<br>
• <strong>201 Created</strong> → Resource was <strong>successfully created</strong> (typically for POST)<br>
• <strong>204 No Content</strong> → Success with no response body (typically for DELETE)<br><br>

Best practice:<br>

```
POST /users → 201 Created
GET  /users → 200 OK
DELETE /users/1 → 204 No Content
```

<strong>A) is incorrect:</strong> 200 is for general success — 201 is more precise for creation.<br>
<strong>B) is incorrect:</strong> 204 means success but with no body returned.<br>
<strong>D) is incorrect:</strong> They are not equivalent — 201 specifically signals creation.

## Question

Which statement about <code>localhost</code> is correct?<br><br>

Please select 1 option<br><br>

A) localhost refers to a remote Tomcat server in the cloud<br>
B) localhost is equivalent to 127.0.0.1 and refers to your own machine<br>
C) localhost is only valid in production environments<br>
D) localhost bypasses the HTTP protocol

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>localhost = 127.0.0.1</strong> = your own computer<br><br>

When you type:<br>

```
http://localhost:8080
```

You are sending an HTTP request <strong>to yourself</strong>.<br><br>

Used for:<br>
• <strong>Local development</strong> — testing before deployment<br>
• Running a Spring Boot app locally<br><br>

<strong>A) is incorrect:</strong> localhost is always local — never remote.<br>
<strong>C) is incorrect:</strong> localhost is a <em>development</em> tool, not for production.<br>
<strong>D) is incorrect:</strong> localhost still uses HTTP — it just routes to the local machine.

## Question

Which of the following correctly describes the relationship between REST and HTTP?<br><br>

Please select 1 option<br><br>

A) REST replaces HTTP with a faster protocol<br>
B) REST is an architectural style that uses HTTP as its transport protocol<br>
C) REST and HTTP are the same thing with different names<br>
D) REST works without HTTP using direct socket connections

## Réponse

<strong>Réponse correcte :</strong> B)<br><br>

<strong>REST uses HTTP — it does not replace it.</strong><br><br>

• <strong>HTTP</strong> = the protocol (the road)<br>
• <strong>REST</strong> = the architectural style (the rules for using the road)<br><br>

A RESTful API:<br>
• Uses <strong>HTTP methods</strong> (GET, POST, PUT, DELETE) semantically<br>
• Uses <strong>status codes</strong> correctly<br>
• Is <strong>stateless</strong> (each request is independent)<br><br>

<strong>A) is incorrect:</strong> REST doesn't replace HTTP.<br>
<strong>C) is incorrect:</strong> They are completely different concepts.<br>
<strong>D) is incorrect:</strong> REST is defined on top of HTTP.

## Question

What is wrong with the following statements about APIs?<br><br>

Please select 2 options<br><br>

A) API ≠ HTTP<br>
B) An API defines the transport layer<br>
C) REST ≠ HTTP<br>
D) HTTP defines the routes of an application<br>
E) An API defines what functionalities are available

## Réponse

<strong>Réponse correcte :</strong> B) et D) — ces deux affirmations sont <strong>incorrectes</strong><br><br>

<strong>Common misconceptions to avoid:</strong><br><br>

❌ <strong>B) An API defines the transport layer</strong><br>
→ WRONG. HTTP defines the transport. The API defines the <em>functionalities</em>.<br><br>

❌ <strong>D) HTTP defines the routes</strong><br>
→ WRONG. HTTP defines how to communicate. The API (your code) defines the routes.<br><br>

✅ Correct statements:<br>
• <strong>API ≠ HTTP</strong> — different concepts<br>
• <strong>REST ≠ HTTP</strong> — REST uses HTTP but is not HTTP<br>
• <strong>An API defines what functionalities are available</strong>
