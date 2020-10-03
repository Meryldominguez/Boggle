let guessForm = $("#guess-form")
let guessFormBtn = $("#guess-form-btn")


async function submitWord(word) {
    let res = await axios.get(`/${word}`)
    cluearray.map(obj=>{       
        let{question,answer,value, showing} = obj;
        showing = null;
        clues.push({question,answer, value, showing})
    })
    let catObj = {title, clues};
    categories.push(catObj);
    return catObj
}
function getWord(){

}

guessFormBtn.onclick(function(){
    
})