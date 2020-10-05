let guessForm = $("#guess-form")
let guessFormBtn = $("#guess-form-btn")
let guessWord = $("#guess")

function getWord(){
    let word = guessWord.val()
    return word.trim()
}


// https://stackoverflow.com/questions/44644290/how-to-properly-submit-form-to-flask-with-ajax

guessForm.on("submit", async function(e){
    e.preventDefault()
    let check = await checkWords()
    guessForm.reset()
    handleResponse(check)
})

async function checkWords(){
    let word = getWord()
    const resp = await axios.post("/check-word",{ word: word });
    console.log(resp)
    return resp.data
}

function handleResponse(resp){
    if (resp.data === "ok"){
    }
    else if (resp.data === "repeat"){}
    else if (resp.data === "not-on-board"){}
    else {}



}