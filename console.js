let buttons = document.querySelectorAll("[onclick]")

for (let i=0; i<buttons.length; i++){
    let button = buttons[i];
    let onclick = button.getAttribute("onclick");
    if (onclick.startsWith("goDownLoadJ")){
        let url = onclick.split("'")
        console.log(url[1])
    }
}