# HTML/CSS Introduction
This project will guide you through how you can use HTML to build web pages. 

## Structure of HTML
The majority of your HTML documents will be made up of tags, which are used to denote HTML elements and define where they are on your page.

In all of the HTML that you will encounter, you will need to add the following tags to begin writing your document:

- `<!DOCTYPE html>`: Used to define the language that is used. The `html` attribute can be changed to use older languages (like HTML4 or XHTML), but for the vast majority of things that you will be doing, this tag will remain the same.
- `<html>`: Used to define the beginning of the HTML code. This is where `<head>` and `<body>` will be nested.
- `<head>`: Used to define the metadata for the document. This is where you would add the title or favicon.
- `<body>`: Used to define the contents of your HTML document. This is where the majority of your code will be.

All together, this is what your HTML documents will look like:

```
<!DOCTYPE html>
<html>
    <head>
        ...
    </head>
    <body>
        ...
    </body>
</html>
```

In this project folder, there is a file called `activity.html` where you will be adding onto for this into project. To open the file in Git Bash, navigate to this folder and type `start ./activity.html`.

You will see that this will open an empty page. For this part of the project, we will be adding titles, favicons, and other pieces of metadata to our template. Complete the following tasks:

- Add a title of your choice to the webpage
- Add a favicon of your choice to the webpage
- Change the author of your webpage to you
- Add a custom description to your webpage

*You won't be able see some of these changes reflected in you web page, why?*

## Elements
While we've learned how to modify the metadata for our site and play around with a few tags, we still have the main part of our HTML page to build out. These are the components that go between the `<body>...</body>` tags and make up what we actually see on our webpage. Each of these components are defined by opening and closing tags along with attributes to define how each of the components function.

These are some of the more common tags that you will encounter:
- `<div>` - A generic HTML container. It is very useful for defining the layout of a page or separating out blocks on elements.
- `<p>` - An HTML paragraph. Used for long blocks of text.
- `<h1>` to `<h6>` - Different levels of header tags. Starting from the largest at `<h1>`, the headers get progressively smaller until `<h6>`.
- `<img>` - HTML element for embedding images.
- `<ul>`, `<ol>`, and `<li>` - Element for different types of lists (ordered, unordered, etc.).

Let's add on to the page we've created in the previous section. Fill out the body to create a template for your new wedsite and add some content (be creative!). Feel free to follow the template given below or create your own. Make sure to add the following elements:

- A header with a title
- Some sort of sidebar or navbar
- A main body where you can add the following:
    - At least one image
    - A body of text (be creative!)
    - A list or table of information
- A footer at the bottom

*Note: For now, just use inline styling*

![sample](images/example.png)

*Hint: You will want to plan out how your page looks beforehand*

*Hint 2: Flexboxes*

## Javascript
So far we've created a webpage and filled it out with some basic information, but we can't really interact with it in any way. You maybe know that there is a `<button>` tag, but (as far as we know) there's no way for it to do anything. To add functionality to our page, we are able to use Javascript and the `<script>` tag to implement event listeners. 

Inside of your `<body>`, you are able to add `<script>` tags to embed client side Javacript code. These can then be added to certain elements of your page as event listeners that will call the function when the event occurs. 



## CSS Styling
styling information

## Big one
 - Take some inspiration from last year for flexboxes
 - This one should cover html, img, hyperlinks, html table, basic javascript (button clicking changing stuff), css styling (padding, margin, size), flexboxes