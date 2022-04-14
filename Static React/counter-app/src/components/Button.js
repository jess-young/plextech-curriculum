import React from 'react';

var Button = (props) => {
    let title = props.title;
    let task = props.title;
    return (
        <button onClick = { task }>{ title }</button>
    );
}

export default Button;