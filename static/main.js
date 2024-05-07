// Events
document.getElementById("btn_idades").addEventListener("click", function(e){
    // console.log("Href -> ", this);
    // e.preventDefault();
    fetch(this.href)
        .then((resp) => resp.json())
        .then(function(data) {
            console.log("Data -> ", data.message);
    }).catch(function(error) {
        console.log(error);
    });
});

function createNode(element) {
    return document.createElement(element);
}

function append(parent, el) {
    return parent.appendChild(el);
}

function index(){
    console.log("bahh");
}

function bindex(){

    const ul = document.getElementById('authors');
    const url = 'https://randomuser.me/api/?results=10';

    fetch(url)
    .then((resp) => resp.json())
    .then(function(data) {
    let authors = data.results;
    return authors.map(function(author) {
        let li = createNode('li');
        let img = createNode('img');
        let span = createNode('span');
        img.src = author.picture.medium;
        span.innerHTML = `${author.name.first} ${author.name.last}`;
        append(li, img);
        append(li, span);
        append(ul, li);
    })
    }).catch(function(error) {
        console.log(error);
    });
}//end function