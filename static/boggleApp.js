let guessForm = $("#guess-form")
let guessFormBtn = $("#guess-form-btn")
let guessWord = $("#guess")
let flashDiv = $("#flash")

function getWord(){
    let word = guessWord.val()
    return word.trim()
}


// https://stackoverflow.com/questions/44644290/how-to-properly-submit-form-to-flask-with-ajax

guessForm.on("submit", async function(e){
    e.preventDefault()
    let check = await checkWords()
    guessWord.val("")
    responseMsg(check)
    handleResponse(check)
})

async function checkWords(){
    let word = getWord()
    const resp = await axios.post("/check-word",{ word: word });
    console.log(resp)
    return resp
}

function responseMsg(resp){
    if (resp.data === "ok"){
        $("<h2>Good one!</h2>")
        .appendTo(flashDiv)
        .addClass("success")
    }
    else if (resp.data === "repeat"){
        $("<h2>Already guessed that one!</h2>")
        .appendTo(flashDiv)
        .addClass("error")
    }
    else if (resp.data === "not-on-board"){
        $("<h2>That one doesnt exist on the board!</h2>")
        .appendTo(flashDiv)
        .addClass("error")
    }
    else if (resp.data === "not-word"){
        $("<h2>Not a word in game...</h2>")
        .appendTo(flashDiv)
        .addClass("error")
    }
    setTimeout(()=>{flashDiv.empty()},1500)
}
function handleResponse(resp){
    word = resp.config.data
    console.log(JSON.parse(word))

}