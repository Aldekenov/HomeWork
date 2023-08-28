function ph() {
    $('input[name="name"]').attr('placeholder', 'Ахалай');
    $('input[name="surname"]').attr('placeholder', 'Махалай');
    $('input[name="birthday"]').attr('placeholder', '2012-12-12');
    $('input[name="number"]').attr('placeholder', '87776665544');
    $('textarea[name="comment"]').attr('placeholder', 'Анау-мынау короче');
}

document.addEventListener("DOMContentLoaded", function (){
    ph()
})