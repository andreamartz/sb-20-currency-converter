### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

    1. Python has official documentation.  JS has very good documentation (MDN is one example), but there's no official documentation source.

    2. Python has to be installed on a machine before it can be used.  With JS, there's nothing to install.

    3. Python has hard releases, and users can use different versions in different virtual environments.  JS releases new features but not new versions.

    4. Python2 is not compatible with Python3. Since JavaScript doesn't have hard releases, there is no direct equivalent in JS.  Features will sometimes be deprecated and then removed entirely from the language, though.

    5. Python does not have type coercion; JS does.  For example, '1' + 3 = 13 in JS, but '1' + 3 results in an error in Python.

    6. Python generates many more errors than JS does.

    7. Python relies on proper indentation to define code blocks; JS uses curly braces ({}).

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

    1. dict_name.get['c']
    2. Use a try/except block like this:
    ```
    try:
        print(dict_name['c'])
    except KeyError:
        print("'c' is not a key in dict_name")
    ```
    3. Use an if block like this:
    ```
    if dict_name['c']:
        print(dict_name['c'])
    ```

- What is a unit test?

    A unit test tests a small piece of functionality in isolation from other pieces of functionality.  For example, a unit test might verify that the value returned from a function is what we expect it to be, given specific arguments.

- What is an integration test?

    An integration test verifies that the units, or individual pieces of code that can be unit tested, are also working _together_ correctly.

- What is the role of web application framework, like Flask?

    Building a web server and setting up routes to respond to requests all from scratch involves a lot of code, and it is very time-consuming.  A web framework can greatly speed up the process by making some decisions for us and taking care of setting up those pieces.  It provides us with functions and classes and other tools that we use out of the box without having to write them ourselves.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

    Passing the information as a resource in the URL is appropriate when there is a view devoted to the content described by that parameter.

    Passing it as part of a query string would be appropriate if the parameter was more of a modifier to get more specific information about the page content than would otherwise be displayed.

- How do you collect data from a URL placeholder parameter using Flask?

- How do you collect data from the query string using Flask?

- How do you collect data from the body of the request using Flask?

- What is a cookie and what kinds of things are they commonly used for?

    A cookie stores small bits of information in the client's browser.  It's a way to save state, since HTTP is a stateless protocol.

    Cookies can be used in countless ways.  A cookie can store a user's id, the items in their shopping cart, the time spent on a page, what ads the user has viewed, or some other small bit of information.

- What is the session object in Flask?

- What does Flask's `jsonify()` do?
