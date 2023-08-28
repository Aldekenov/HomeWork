function num() {
    // for (let i = 0; i < 4; i++) {
        n = $('#ph_num')
        nt = n.text()
        n.text(`${nt[0]} (${nt[1]}${nt[2]}${nt[3]}) ${nt[4]}${nt[5]}${nt[6]} ${nt[7]}${nt[8]}${nt[9]}${nt[10]}`)
        // console.log($('[id=ph_num]').length);
    // }
}

document.addEventListener("DOMContentLoaded", function (){
    num()
})