# Counter App

## Intro

React, a JavaScript library for creating interactive user interfaces (UIs) is getting more popular by developers all around the world. Here are some useful terms:

1. **Components** – We do not have pages in a React app - it only contains components. React components are small reusable pieces of code that return React elements in a format that we call *JSX*.

2. **States** – Some components may need to store some values/variables. So *states* are used to store these variables which are specific for a component. When a component is mounted, the states associated with the component also load. Then, we can access and set the values stored in that state.

3. **Props** – There may be two or more components in a React app. So if we need to pass a value/state from one component to another, *props* are used.

## Resources 

Refer to this great official [React tutorial](https://reactjs.org/tutorial/tutorial.html).
Note: Many things here might use the older class-based components, while the newer approach is to use functional components with Hooks.

Also feel free to use online resources such as Stack Overflow, MDN, W3, and Google for reference.

## A Note on Collaboration

This is a partner project! You will both be keeping up with your own versions of the code, but should work through this assignment together with constant communication.

## Setup

1. Pull the starter code
    - `git pull starter main`

2. Make sure you have npm installed

3. Go into this directory
    - `cd "Static React"`

4. Initialize an empty react app
    - `npm install create-react-app`
    - `npx create-react-app counter-app`

5. Start the React server
    - `cd counter-app`
    - `npm start`

## Your Task

[Here's what we'll be building](https://i1.wp.com/www.techomoro.com/wp-content/uploads/2020/04/counter-app-working.gif?fit=640%2C335&ssl=1):

![https://i1.wp.com/www.techomoro.com/wp-content/uploads/2020/04/counter-app-working.gif?fit=640%2C335&ssl=1](https://i1.wp.com/www.techomoro.com/wp-content/uploads/2020/04/counter-app-working.gif?fit=640%2C335&ssl=1)

It's kinda ugly. Feel free to use your creativity to make it prettier!

## Walkthrough

In this section, we'll be going through a soft tutorial for how to build the application. If you want more of an exploratory challenge, feel free to skip this and stick it out on your own!

### Step 1: Create a button

We need two buttons for the view. An increment(+) button and a Decrement button(-). 

Both of these buttons are pretty similar - so we should create a Component to encompass the code that we can simply reuse across these 2 buttons.

Within the filesystem, lets create a `Button.js` file inside a `src/components` directory (create it if it doesn't exist) to be a reusable Button component. This will have to be imported into your main view!

We will be getting the values from the main component (`App.js`) as props. What kind of values will we need? Think about what will differ between the 2 Increment and Decrement buttons.

## Caution: Spoiler Solution!
For just this problem, let's go into the solution.
```JSX
// components/Button.js
import React from 'react';

var Button = ({title, task}) => {
    return (
        <button onClick = { task }>{ title }</button>
    );
}

export default Button;
```
Let's break this down:

1. `import React from 'react';`

    First, we import React. Do this in every React file.

2. `var Button = ({title, task}) => {`
    This is a lambda funcion, assigned to the name Button. 
    The {} parameter syntax means the parameter is an object with attributes `title` and `task`.
    So if `{title: "hello", task: "world", key:"value"}` is what is passed as the props, `title` is set to "hello" and `task` is set to "world" within the local scope of the function. This is a shortcut equivalent to:

```JSX
    var Button = (props) => {
        let title = props.title;
        let task = props.task;
        // ...
    }
```

3. `return ( <button onClick = { task }>{ title }</button> )`

    We need to return a [JSX](https://www.geeksforgeeks.org/jsx-full-form/#:~:text=JSX%20stands%20for%20JavaScript%20XML,the%20full%20power%20of%20JavaScript.) value from the render() function. Remember that anytime we need to input JavaScript into the JSX we have to use `{}` and put our JavaScript in there.

    
\* *Note: If we format our Component as a *function*, everything (state management, props, etc.) will be a [little different](https://medium.com/star-gazers/react-class-vs-functional-components-a49383f65f0e). For the scope of this class, we will prefer and support the use of Components as **classes**, for standardization.*

4.  `export default Button;`
    In ES6 there are two kinds of exports:

    **Named exports** - for example `export class A extends Component {...}` is a named export with the name of "A". Named modules can be imported using `import { exportName } from 'module';`. In this case, the name of the import should be the same as the name of the export. To import the class in the example, you'll have to use `import { A } from 'component.js';`. There can be multiple named exports in one module.

    **Default export** - is the value that will be imported from the module, if you use the simple import statement `import X from 'module'`. "X" is the name that will be given locally to the variable assigned to contain the value, and it doesn't have to be named like the origin export. *There can be only one default export*.

    A module can contain both named exports and a default export, and they can be imported together using `import defaultExport, { namedExport1, namedExport3, etc... } from 'module';`.

### Step 2: State Operations

We need to manage the state within `App.js`. What state variables will we need? Think about what's dynamic in our application. 

    **Spoiler**: If you said the count, you're absolutely right! This is the only thing that changes within our page. 

First, find where in our Component we can *initialize* our state. 

    **Spoiler**: If you said the constructor, you're absolutely right! The constructor gets called whenever the Component gets created. Thus, all our initialization stuff, including setting up the state, should go here.

Then, figure out what functions we need to *modify* our state.

    **Spoiler**: If you said something along the lines of incrementCount() and decrementCount(), you're absolutely right! Remember that we have 2 distinct operations with our count. *Add* one to the count, and *Subtract* one from the count. You can also create just one function with a parameter if you handle the logic correctly.

Now you have everything you need to set up your state management within the `App.js` class component!

### Step 3: Main View

Now, at last, we need a view. As previously describes, in React, we define views as functional components. This component will be re-rendered at every state change.

In this project, we have added two Button components with values + and -, and a count variable inside the `h2` tag. You can see that the count variable is actually the state count that we defined earlier.

### Discussion on the "task" prop
What's our desired task when each button gets clicked? How can we use the Button component that we defined earlier?

Then, we make use of our Button component we created earlier to simply pass in the button text and the function we want to call. We pass these in as JavaScript variables.

Assume we have implemented a function `incrementCount()` in scope in the main view component.

Let's take a deeper look at how we pass in the function from the main view component. One idea is:

    task = { () => incrementCount() }

Here, we are actually passing in the pointer to a function that just calls incrementCount(). Why are we doing it this way?

We don't actually have to! In fact, we could totally just do:

    task = { incrementCount }

But why can't we do:

    task = { incrementCount() }

The second option executes the function, returns the value and passes *that* into task. That's not our desired functionality! We want to pass in the actual function so we can execute that later (in this case, when the button is pressed), not what it returns.

### Congrats!

You're all done with the project :) Make sure you add fun styles (if you want)
