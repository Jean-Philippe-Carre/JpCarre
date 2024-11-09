function playTheGame() {
  let userResponse = confirm("Would you like to play the game? ");
  if (userResponse === true) {
    let userInput = prompt("Enter a number between 0 and 10: ");
    let randomNumber = Math.random() * 2;
    console.log(randomNumber);

    if (userInput === randomNumber) {
      alert("Congrats!! you won!!");
    } else if (userInput != number) {
      alert("Sorry it's not a number, goodbye...");
    } else if (userInput < 0 || userInput > 2) {
      alert("Enter a valid number between 0 and 10.");
    } else {
      alert("Wrong guess...");
    }
  } else {
    alert("No problem, goodbye...");
  }
}
