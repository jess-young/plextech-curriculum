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

You are able to customize the function of your tags using attributes. Most notably, you are able to use the `style` attribute with many of your tags to change the appearance or formatting of the tag, with each style attribute separated with semicolons. 

Let's add on to the page we've created in the previous section. Fill out the body to create a template for your new website and add some content. Please follow the template given below. Make sure to add the following elements:

- A header with a title
- Some sort of sidebar or navbar
- A main body where you will incorporate many images
- A footer at the bottom'

- Use flexboxes for positioning, check out how to use it and what it is here: [Guide to FlexBoxes](https://css-tricks.com/snippets/css/a-guide-to-flexbox/). You will use this more later.

*Note: For now, just use inline styling*

![sample](images/example.png)

*Hint: You will want to plan out how your page looks beforehand*

## Javascript
So far we've created a webpage and filled it out with some basic information, but we can't really interact with it in any way. You maybe know that there is a `<button>` tag, but (as far as we know) there's no way for it to do anything. To add functionality to our page, we are able to use Javascript and the `<script>` tag to implement event listeners. 

While this project isn't specifically about Javascript, there is some syntax that you should know before adding script into your HTML.

In Javascript, variables are declared with keywords that define what you are able to do with them. These keywords are `const`, `var`, and `let`. The `const` keyword sets the reference of the variable to be read-only, so that reassigning its referene is not allowed. On the other hand `var` and `let` allows you to change the reference and only differ in the scope of which the variables are declared. For the purposes of this project, you don't need to know the difference.

Functions are defined with the `function` keywords, along with the name and parameters:

```
function name(p1, p2) {
    // BODY
}
```

In order to reference the elements in your page, you will need to use the `document` objects, which is a predefined variable that refers to the HTML page. So if you want to change a specific element within your page, you would refer to it with `document.getElementById(id)`. *There are many other things you can do with it.* 

Inside of your `<body>`, you are able to add `<script>` tags to embed client side Javacript code. These can then be added to certain elements of your page as event listeners that will call the function when the event occurs. For instance, consider the following block of code:

```
<script>
    let d = new Date();
    document.body.innerHTML = "<h1>Today's date is " + d + "</h1>"
</script>
```

Adding this to the body will display today's date in `<h1>` tags. Additionally, you can define the `id` attribute of your elements and refer to that elements using `document.getElementById(id)`. Then, you are able to define a function under `<script>` and attach it to a button's `onclick` event listener. For example, the following will chance the color style attribute of the `<p>` element on a button press.

```
<p id="demo">click on the button</p>
<button onclick="green()">Change to green</button>
<script>
    function green() {
        var el = document.getElementById("demo");
        el.style.color="#00FF00";
    }
</script>
```

Now lets add some scripts to make your page more interactive. Your task is to add two buttons in your header that will enable a "light" and "dark" mode for your page. These modes should change the background colors and font colors of the page. Feel free to choose your colors as you wish, but make sure to incorporate a variety of different shades for each theme. 

## CSS Styling
The last thing that we will be covering is CSS. In general, there are three types of CSS that you can apply to your HTML web page. 

- Inline - Adding styling within the `style` attribute of the element
- Internal - Adding styling within the `<style>` tag
- External - Adding styling within a CSS file and linking to with a `<link>` tag

So far, you've only used inline styling to style your pages. However, you can probably see how this can become more and more messy. Internal styling improves upon this by moving the styles that you apply into a separate section within your code. But ideally, you would want to move your styling into a different file completely and link the sheet to your HTML page. This will help with readability, reduce redundancies in your code, and is just generally a good coding practice.

All CSS files end with the `.css` extention. These files will look very different from a lot of other code you might have written. These style sheets consist of a series of selectors, which you use to choose what to apply your styling to, and the actual styling. So the file will look something like this:

```
p {
    color: green
}

.example {
    font-size: 30px
}

div > h1 {
    color: red
}
```

Let's break these down. 

The `p` selector selects all `<p>` tags and applies the styling to those elements. If you want to apply the same styling to multiple tags, you can chain the selectors together with spaces (if you want to also apply it to `h1`, the selector would be `p h1`). 

The `.example` selector selects all elements with the `example` class name. These would be those with `example` as an element's `class` attribute. Similar to the element selectors, you are able to chain these to apply the stylings with different classes. Instead of spaces, these selectors would be separated with `.`. (ex. `.example.other` applies the styling to classnames `example` and `other`). You can also apply several classnames to a single elements. For example, `class="example other"` applies the styles associated with `example` and `other`.

Finally, the `div > h1` selector selects all `h1` elements that is a child of a `div`. So if your HTML looks like this:

```
<h1>Hello</h1>
<div>
    <h1>World</h1>
</div>
```

Only "World" would be styled.

Of course, this is just a small sample of all the selectors and styles that you can apply. If there is something specific that you want to style in a certain way, you should check out a reference sheet for CSS.

In order to finally link your sheet into your HTML, you will need to use a `<link>` element at the `head` of your file (`<link rel="stylesheet" href="example.css">`).

Now, transfer your inline styles into an external style sheet.

---

# Divs and Rectangles

## Intro

Now that you understand some of the basics of HTML and CSS, let’s take a look at how to align HTML elements. There are multiple ways to align HTML elements, but in this part, we recommend using flexboxes as they are widely used in modern web development (for example BootstrapV4 is built on top of flexboxes).

## Resources 

Refer to this great webpage on how to use flexboxes: [CSS Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/).

Also feel free to use online resources such as Stack Overflow, MDN, W3, and Google for reference.

## Your Task

When you open the provided HTML file `part1/index.html` , it should look like this:

![part1-initial-look.png](images/part1-initial-look.png)

As you can see, there are 9 rectangles. The styling and makeup of the first two rectangles are already built for you. 

**Your task is to apply stylings and add div elements inside of the next 7 green rectangular blocks to create a webpage that looks like this:**

![part1-finished-look.png](images/part1-finished-look.png)

Note that these rectangular blocks should be *responsive*. Here is what they look like when the window is thinner:

![part1-finished-narrowed-look.png](images/part1-finished-narrowed-look.png)

## Row Information

3. For the third row, the red and blue end rectangles should remain the same width, and the green space should shrink.

    *Possible Approach: Have a div with a red background and a div with a blue background, both with fixed width. Use an appropriate value for Justify Content.*

4. For the fourth row, the blue end rectangle should remain the same width, and the red rectangle should shrink.

    *Possible Approach: Have a div with a red background and a div with a blue background. Have a fixed width on the blue div. Use Flex Grow.*

5. For the fifth row, the red square should remain the same size, but always remain in the center of the green rectangle.

    *Hint: Think about how to keep a div fixed size and how to align something in the absolute center of the parent element.*

6. For the sixth row, the blue rectangle should remain the same size, while the red rectangles should shrink. The blue rectangle should remain in the center of the row.

    *Hint: Use two red divs.*

7. For the seventh row, the red rectangle should remain the same width.

    *Hint: Nest divs and use background-color: transparent*

8. For the eighth row, the orange rectangles should remain the same size while the green space between them shrinks.

9. For the ninth row, the green space between the orange rectangles should remain the same width while the orange rectangles narrow.

## Additional Information

You should only have to use the div html element to complete this assignment. Also, none of the divs you create inside of the provided wrapper divs should have `background-color: green;`. But it is valid to specify non-green background colors for any divs, including the wrapper.

Try to style the boxes as closely to the solution image as possible don't worry about getting exact dimensions or rgb values. We care about what structure, CSS styles you used, and the dynamic behavior of the page. However just for reference,

- The color of the boxes we used are `background-color: red` , `blue` , and `orange`

- Some width/height values we used are `20px`, `40px`, `80px`

## Contributions
Thank you to Brown University's CSCI 1320 for providing the spec and the starter code.
