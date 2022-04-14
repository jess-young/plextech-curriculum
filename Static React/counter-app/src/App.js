// import App from './App';
// import 'App.css';
import { useState } from 'react';

function ButtonIncrement(props) {
  
  return (
    <button style={{ margin: '0.5rem'}} onClick={props.onClickFunc}>
    +
    </button>
  )
}
function ButtonDecrement(props) {
 
 return (
   <button style={{ margin: '0.5rem'}} onClick={props.onClickFunc}>
   -
   </button>
 )
}
function Display(props) {
 return (
   <label style={{ margin: '0.5rem'}} >{props.message}</label>
 )
}

function App() {
  const [count, setCount] = useState(1);
  const incrementCount = () => setCount(count + 1);
  const decrementCount = () => setCount(count - 1);

  return (
    <div className="App">
      <ButtonDecrement onClickFunc={() => decrementCount()}/>
      <Display message={count}/>
      <ButtonIncrement onClickFunc={() => incrementCount()}/>
    </div>
  );
}

export default App;
