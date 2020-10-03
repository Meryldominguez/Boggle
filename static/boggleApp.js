let guessForm = $("#guess-form")
let guessFormBtn = $("#guess-form-btn")
let guessWord = $("#guess")

function handleWord(){
    let word = guessWord.val()
    
    return word.trim()
}

// https://stackoverflow.com/questions/44644290/how-to-properly-submit-form-to-flask-with-ajax

guessForm.on("submit", async function(e){
    e.preventDefault()
    let word = handleWord()
    const resp = await axios.get("/check-word", { params: { word: word }});
})
