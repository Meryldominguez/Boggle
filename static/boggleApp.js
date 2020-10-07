let $guessForm = $("#guess-form")
let $guessFormBtn = $("#guess-form-btn")
let $guessWord = $("#guess")
let $flashDiv = $("#flash")
let $wordDiv = $("#word-div")
let $wordList = $("#word-list")
let $scoreDiv = $("#score")
let $timer = $("#time")

class Boggle{
    constructor(minutes){
        this.time = minutes*60000
        this.list=[]
    }
    getWord(){
        let word = $guessWord.val()
        return word.trim()
    }
    async checkWords(){
        let word = this.getWord()
        if (word == false){
            word = {'data':false}
            return this.responseMsg(word)
        }else{
        const resp = await axios.post("/check-word",{word: word});
        return resp
        }
    }
    responseMsg(resp){
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
        setTimeout(()=>{$flashDiv.empty()},1500)
    }

    // async getWordList(){
    // let resp = await axios.get("/wordlist")
    // return resp.data
    // }
    renderWordList(list){
    $wordList.empty()
    for (let word of list){
        $(`<li>${word}</li>`)
            .appendTo($wordList)
    }
    return list
    }
    async getScore(){
        let resp = await axios.get("/score")
        return resp.data
    }
    renderScore(val){ 
        $scoreDiv.text(`${val}`)
    }

    async updateHighScore(){
        let finalScore = $scoreDiv.text()
        const resp = await axios.post("/score",{ score : finalScore });
    }
    async handleResponse(resp){
        let word = JSON.parse(resp.config.data).word
        

        this.list.push(word)
        this.renderWordList(this.list)
        let score = await this.getScore()
        this.renderScore(score)
        await this.updateHighScore()
    }
    timer(){
        let timer = setInterval(()=>{
            this.time = this.time - 1000
            $timer.text(`${(this.time)/1000} seconds`)
            if (this.time === 0){
            clearInterval(timer)
            this.endGame()
        }
        },1000)}
        
    endGame(){
        $guessForm.empty()
        this.endGameMessage()
    }
    endGameMessage(){
        $("<h2>Good Game!!</h2>")
            .appendTo($flashDiv)
            .addClass("success")
        $(`<button>Play again?</button>`)
            .appendTo($flashDiv)
            .on('click',()=>{
            window.location.reload(true)})
            .addClass("success")
    }
}


$(async function(){
    const game = new Boggle(1)
    game.timer()
    $guessForm.on("submit", async function(e){
        e.preventDefault()
        let check = await game.checkWords()
        $guessWord.val("")
        game.responseMsg(check)
        if (check.data === "ok"){
            await game.handleResponse(check)
        }
    })
    
    })