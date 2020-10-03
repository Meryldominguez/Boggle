let guessForm = $("#guess-form")
let guessFormBtn = $("#guess-form-btn")
let guessWord = $("#guess")

function handleWord(){
    let word = guessWord.val()
    return word
}


// https://stackoverflow.com/questions/44644290/how-to-properly-submit-form-to-flask-with-ajax

guessForm.on("submit", async function(e){
    e.preventDefault()
    let word = handleWord()
    $.post("/", {word:word})
})

class Boggle{
    constructor(){

    }
    function submitWord(self) {
        
    }
}