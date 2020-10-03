let guessForm = $("#guess-form")
let guessFormBtn = $("#guess-form-btn")
let guessWord = $("#guess")



// async function submitWord(word) {
//     let res = await axios.post(`guess/${word}`)
 
//     return res.data.message
// }



// https://stackoverflow.com/questions/44644290/how-to-properly-submit-form-to-flask-with-ajax

guessFormBtn.on("submit", async function(e){
    e.preventDefault()
    let word = handleWord()
    $.ajax({
      type: 'get',
      url: `/wordcheck`,
      data: word
      });
})
