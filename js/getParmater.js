var s = 1;
function getParmater(dat) {
    var Adat = new Map();
    dat = dat.split("&&");
    // console.log(dat);
    dat.forEach(function (each) {
        /*console.log(each);*/
        Adat[each.split("=")[0]] = each.split("=")[1];
    });
    return Adat;
}

