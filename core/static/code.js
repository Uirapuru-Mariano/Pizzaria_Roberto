// 1. Select all elements with the class name 'myButtonClass'
const descs = document.querySelectorAll('.desc');

// 2. Define the function that will be executed when the event occurs
function handleButtonClick(event) {
  alert('Button clicked! The button text is: ' + event.target.textContent);
  // You can add more logic here
}

// 3. Loop through the NodeList and add the listener to each element
buttons.forEach(button => {
  button.addEventListener('click', handleButtonClick);
});
