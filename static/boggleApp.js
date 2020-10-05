let $guessForm = $("#guess-form")
let $guessFormBtn = $("#guess-form-btn")
let $guessWord = $("#guess")
let $flashDiv = $("#flash")
let $wordDiv = $("#word-div")
let $wordList = $("#word-list")
let $scoreDiv = $("#score")

function getWord(){
    let word = $guessWord.val()
    return word.trim()
}

// https://stackoverflow.com/questions/44644290/how-to-properly-submit-form-to-flask-with-ajax

guessForm.on("submit", async function(e){
    e.preventDefault()
    let check = await checkWords()
    $guessWord.val("")
    responseMsg(check)
    await handleResponse(check)
})

async function checkWords(){
    let word = handleWord()
    const resp = await axios.post("/check-word",{ word: word });
    return resp
}

function responseMsg(resp){
    if (resp.data === "ok"){
        $("<h2>Good one!</h2>")
        .appendTo($flashDiv)
        .addClass("success")
    }
    else if (resp.data === "repeat"){
        $("<h2>Already guessed that one!</h2>")
        .appendTo($flashDiv)
        .addClass("error")
    }
    else if (resp.data === "not-on-board"){
        $("<h2>That one doesnt exist on the board!</h2>")
        .appendTo($flashDiv)
        .addClass("error")
    }
    else if (resp.data === "not-word"){
        $("<h2>Not a word in game...</h2>")
        .appendTo($flashDiv)
        .addClass("error")
    }
    else{
        $("<h2>Please enter a word</h2>")
        .appendTo($flashDiv)
        .addClass("error")
    }
    setTimeout(()=>{flashDiv.empty()},1500)
}
async function handleResponse(resp){
    let word = JSON.parse(resp.config.data)
    console.log(word.word)
    let list = await getWordList()
    renderWordList(list)
    let score = await getScore()
    renderScore(score)
}
async function getWordList(){
    resp = await axios.get("/wordlist")
    return resp.data
}
function renderWordList(list){
    wordList.empty()
    for (word of list){
        $(`<li>${word}</li>`)
            .appendTo($wordList)
    }
    return list
}
async function getScore(){
    resp = await axios.get("/score")
    return resp.data
}
function renderScore(val){ 
    $scoreDiv.text(`<h2>${val}</h2>`)
}