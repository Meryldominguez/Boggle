let guessForm = $("#guess-form")
let guessFormBtn = $("#guess-form-btn")
let guessWord = $("#guess")



async function submitWord(word) {
    let res = await axios.post(`guess/${word}`)
 
    return res
}

function getWord(){
    if (guessWord.val()){
        return guessWord.val()}
    else{
        alert("please guess a word!")
    }
}

guessFormBtn.onclick(async function(e){
    e.preventDefault()
    let word = getWord()
    await submitWord(word)


})