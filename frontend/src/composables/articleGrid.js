export default function articleGrid() {
    const imageIfExists = (article) => {
        return _imageIfExists(article)
    };
    const gridStyle = (article) => {
        return _gridStyle(article)
    };
    return {
        imageIfExists,
        gridStyle,
    }
}

function findmedia(urlimage){
    let media="/media/";
    let inmedia=-1;
    for(let i=0;i<urlimage.length;i++){
        if(inmedia!=-1) break;
        if(urlimage[i]=='/'){
            // console.log(urlimage.substring(i,i+7),inmedia);
            if(urlimage.substring(i,i+7)===media){
                inmedia=i;
            }
        }
    }
    let urlnow="http://112.74.87.154:8004";
    if(inmedia==-1){
        return urlimage;
    }
    let urladd=urlimage.substring(inmedia,urlimage.length);
    urlnow=urlnow+urladd;
    return urlnow;
}

function _imageIfExists(article) {
    if (article.avatar) {
        // console.log(article.avatar.content);
        let urlimage=article.avatar.content;
        // console.log(findmedia(urlimage));
        let urlfinal=findmedia(urlimage);
        console.log(urlfinal)
        return urlfinal
    }
}
function _gridStyle(article) {
    if (article.avatar) {
        return {
            display: 'grid',
            gridTemplateColumns: '1fr 4fr'
        }
    }
}