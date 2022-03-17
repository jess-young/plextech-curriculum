# Divs and Rectangles

## Intro

Now that you understand some of the basics of HTML and CSS, let’s take a look at how to align HTML elements. There are multiple ways to align HTML elements, but in this part, we recommend using flexboxes as they are widely used in modern web development (for example BootstrapV4 is built on top of flexboxes).

## Resources 

Refer to this great webpage on how to use flexboxes: [CSS Flexbox Guide](https://css-tricks.com/snippets/css/a-guide-to-flexbox/).

Also feel free to use online resources such as Stack Overflow, MDN, W3, and Google for reference.

## A Note on Collaboration

This is a partner project! You will both be keeping up with your own versions of the code, but should work through this assignment together.

## Setup

1. Clone your Personal Repository

    If you haven't already, clone the GitHub repository that you set up in our Kickoff Meeting to your local file system. You can do this by:

    - Opening Git Bash within the folder you want to clone into
    - `git clone https://github.com/<USERNAME>/fa21-plextech-<firstname>.git`
    - cd `fa21-plextech-<firstname>.git`

2. Add the Starter Code Remote

    - `git remote add starter https://github.com/AkshatJain1/fa21-plextech-fswd.git`

3. Pull the starter code
    - `git pull starter main`

4. Push to your Github
    - `git add .`
    - `git commit -m "Added starter code for Divs and Rectangles"`
    - `git push origin main`

## Your Task

When you open the provided HTML file `part1/index.html` , it should look like this:

![part1-initial-look.png](part1-initial-look.png)

As you can see, there are 9 rectangles. The styling and makeup of the first two rectangles are already built for you. 

**Your task is to apply stylings and add div elements inside of the next 7 green rectangular blocks to create a webpage that looks like this:**

![part1-finished-look.png](part1-finished-look.png)

Note that these rectangular blocks should be *responsive*. Here is what they look like when the window is thinner:

![part1-finished-narrowed-look.png](part1-finished-narrowed-look.png)

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

You are not required to use Bootstrap in this part. You can use if you want, but we actually recommend writing plain CSS. Just for this part, inline CSS is acceptable, but you should generally avoid using inline CSS in the future.

## Contributions
Thank you to Brown University's CSCI 1320 for providing the spec and the starter code.