function creatediapo(str) {
    console.log(str)
    const itemdiapo = document.getElementById('itemdiapo')
    itemdiapo.src = "str"
    document.getElementById('detailImage').hidden = false
}
function closediapo(){  
    const itemdiapo = document.getElementById('itemdiapo')
    itemdiapo.src = ""
    document.getElementById('detailImage').hidden = true
}

function openBox(){
    document.getElementById('buttonChatbot').classList.replace('block', 'hidden')
    document.getElementById('messagerChatbot').classList.replace('hidden', 'block')
}

function closeBox(){
    document.getElementById('buttonChatbot').classList.replace('hidden', 'block')
    document.getElementById('messagerChatbot').classList.replace('block', 'hidden')
}