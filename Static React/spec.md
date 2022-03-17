# Counter App

## Intro

React, a JavaScript library for creating interactive user interfaces (UIs) is getting more popular by developers all around the world. Here are some useful terms:

1. **Components** – We do not have pages in a React app - it only contains components. React components are small reusable pieces of code that return React elements in a format that we call *JSX*.

2. **States** – Some components may need to store some values/variables. So *states* are used to store these variables which are specific for a component. When a component is mounted, the states associated with the component also load. Then, we can access and set the values stored in that state.

3. **Props** – There may be two or more components in a React app. So if we need to pass a value/state from one component to another, *props* are used.

## Resources 

Refer to this great official [React tutorial](https://reactjs.org/tutorial/tutorial.html).

Also feel free to use online resources such as Stack Overflow, MDN, W3, and Google for reference.

## A Note on Collaboration

This is a partner project! You will both be keeping up with your own versions of the code, but should work through this assignment together with constant communication.

## Setup

1. Pull the starter code
    - `git pull starter main`

2. Install dependencies
    - `cd counter-app`
    - `npm install`

3. Start the React server
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

Within the filesystem, lets create a `Button.js` file inside an `src/components` directory to be a reusable Button component.

We will be getting the values from the main component (`App.js`) as props. What kind of values will we need? Think about what will differ between the 2 Increment and Decrement buttons.

## Caution: Spoiler Solution!
```
// components/Button.js

import React, { Component } from 'react'
export default class Button extends Component {
    render() {
        let { title, task } = this.props;
        return (
            <button onClick = { task }>{ title }</button>
        );
    }
}
```
Let's break this down:

1. `import React, { Component } from 'react'`

    First, we import React and the Component. We always have to do this in every *class* component \*. 

2. `export default class Button extends Component`
    Then, we write our class header which will follow this format. Here are a few pointers for exporting classes in JavaScript: 
    
    - If we want to create a private, helper component (only accessible within the same file), don't `export` it.
    
        For example, this implementation is also valid (but very unnecessary and code-heavy): 

        ```
        // Button.js

        import React, { Component } from 'react'

        class Description extends Component {
            let {text} = this.props; // take in text from props
            render() {
                return (
                    <p>{text}</p> 
                ); 
            }
        }

        export default class Button extends Component {
            render() {
                let { title, task } = this.props;
                return (
                    <button onClick = { task }>
                        <Description text={title} />
                    </button>
                );
            }
        }
        ```

        The `Description` component will not be recognized outside the `button.js` file. This is what we call a "Private Component".

    - We can export multiple things inside a file:

        ```
        // component.js

        export class A extends Component {...}
        export default class B extends Component {...}

        // main.js
        import B, {A} from 'component.js';
        ```

        In ES6 there are two kinds of exports:

        **Named exports** - for example `export class A extends Component {...}` is a named export with the name of "A". Named modules can be imported using `import { exportName } from 'module';`. In this case, the name of the import should be the same as the name of the export. To import the class in the example, you'll have to use `import { A } from 'component.js';`. There can be multiple named exports in one module.

        **Default export** - is the value that will be imported from the module, if you use the simple import statement `import X from 'module'`. "X" is the name that will be given locally to the variable assigned to contain the value, and it doesn't have to be named like the origin export. *There can be only one default export*.

        A module can contain both named exports and a default export, and they can be imported together using `import defaultExport, { namedExport1, namedExport3, etc... } from 'module';`.

3. `render() {}`

    Within every React class component, we need to define a `render` function. **Important: Everytime the state changes, the component will `render()` again**

    The return value of this function will be some JSX that will be rendered on the webpage.

4. `let { title, task } = this.props;`

    `this.props` is an object that is passed into each instance of the React Component. This JS syntax is called "destructring". This is the exact same as doing:

    ```
    let title = this.props.title;
    let task = this.props.task;
    ```

5. `return ( <button onClick = { task }>{ title }</button> )`

    We need to return a [JSX](https://www.geeksforgeeks.org/jsx-full-form/#:~:text=JSX%20stands%20for%20JavaScript%20XML,the%20full%20power%20of%20JavaScript.) value from the render() function. Remember that anytime we need to input JavaScript into the JSX we have to use `{}` and put our JavaScript in there.

    
\* *Note: If we format our Component as a *function*, everything (state management, props, etc.) will be a [little different](https://medium.com/star-gazers/react-class-vs-functional-components-a49383f65f0e). For the scope of this class, we will prefer and support the use of Components as **classes**, for standardization.*


### Step 2: State Operations

We need to manage the state within `App.js`. What state variables will we need? Think about what's dynamic in our application. 

    **Spoiler**: If you said the count, you're absolutely right! This is the only thing that changes within our page. 

First, find where in our Component we can *initialize* our state. 

    **Spoiler**: If you said the constructor, you're absolutely right! The constructor gets called whenever the Component gets created. Thus, all our initialization stuff, including setting up the state, should go here.

Then, figure out what functions we need to *modify* our state.

    **Spoiler**: If you said something along the lines of incrementCount() and decrementCount(), you're absolutely right! Remember that we have 2 distinct operations with our count. *Add* one to the count, and *Subtract* one from the count. You can also create just one function with a parameter if you handle the logic correctly.

Now you have everything you need to set up your state management within the `App.js` class component!

## Caution: Spoiler Solution!

```
// App.js

import React, { Component } from 'react';

export default class App extends Component {
    constructor(){
        super();

        this.state= {
            count: 0
        };
    }

    // Main Solution
    incrementCount = () => {
        this.setState({
            count: this.state.count + 1
        });
    }

    decrementCount = () => {
        this.setState({
            count: this.state.count - 1
        });
    }

    // Alternatively
    doCount = (isAdd) => {
        this.setState({
            count: this.state.count + (isAdd ? 1 : -1)
        });
    }
}
```

Let's break this down!

1. Constructor

    First, we make a call to `super()`. We always have to do this whenever we define the constructor. Next, we initialize the `state` just like we're making a normal JS object. Don't be fooled by this simplicity though - the `state` variable is very powerful!

2. Increment/Decrement Count

    We use `this.setState()` to update the state with whatever's in the object that's passed as a parameter. Remember that this will refresh the component and any code immediately after the `this.setState()` within the same function frame would reflect the **old** value.


### Step 3: Main View

Now, at last, we need a view. As previously describes, in React, we define views inside `render()` function. The render will get executed with each state or prop change. We return the value as a JSX value.

In this project, we have added two Button components with values + and -, and a count variable inside the `h2` tag. You can see that the count variable is actually the state count that we defined earlier.

What's our desired task when each button gets clicked? How can we use the Button component that we defined earlier?

## Caution: Spoiler Solution!

```
render() {
  let { count } = this.state
  return (
    <div>
      <h2>Count: { count } </h2>
      <Button
        title = { "+" }
        task = { () => this.incrementCount() }
      />
      <Button
        title = { "-" }
        task = { () => this.decrementCount() }
      />
     </div>
  );
}
```

We don't really *need* to define `count` as a local variable. The code will totally work if just use `this.state.count` in the `h2` content instead. This is just cleaner code though.

Then, we make use of our Button component we created earlier to simply pass in the button text and the function we want to call. We pass these in as JavaScript variables.

Let's take a deeper look at how we pass in the function

    task = { () => this.incrementCount() }

Here, we are actually passing in the pointer to a function that just calls incrementCount(). Why are we doing it this way?

We don't actually have to! In fact, we could totally just do:

    task = { this.incrementCount }

But why can't we do:

    task = { this.incrementCount() }

The second option executes the function, returns the value and passes *that* into task. That's not our desired functionality! We want to pass in the actual function so we can execute that later (in this case, when the button is pressed), not what it returns.

This presents a unique issue:

What happens if we want to use our alternative solution as pass in a variable instead? As just described, This won't work:

    task = { this.doCount(true) }

And we can't just use doCount without the parameter.

So this won't work either:

    task = { this.doCount }

To solve this issue, we define a new "throwaway" function that calls the `doCount` function.

    task = { () => this.doCount(true) }

`doCount` will not get executed right away now, and it has a parameter!

Note: Is this valid?:

    task = { (() => this.doCount(true))() }

### Congrats!

You're all done with the project :) Make sure you add fun styles (if you want), and push to GitHub so we can see it too!
