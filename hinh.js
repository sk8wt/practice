///CODE TO PULL IN PARTS
var spData = null;

function doData(json) {
    spData = json.feed.entry;
}

function readData($partsContent) {

    const startCol = 2;

    var data = spData;
    var divData = [];
    var row = 0;

    for (var i = 0; i < data.length; i++) {
        var cell = data[i]["gs$cell"];
        var val = cell["$t"];
        console.log(val);
        if (cell.col == startCol) {
            drawDiv(divData, $partsContent, (row == 1));
            divData = [];
            row++;
        }
        divData.push(val);
    }
    drawDiv(divData, $partsContent);
}

function drawDiv(divData, parent, isHeader) {
    if (divData == null) return null;
    if (divData.length == 0) return null;
    if (isHeader) return;

    partNum = divData[0];
    imgURL = divData[1];
    mfr = divData[2];
    model = divData[3];
    type = divData[4];
    price = divData[5];
    avail = divData[6];
    orders = divData[7];

    //Write parts-content div
    var $partsDiv = jQuery("<div/>");
    $partsDiv.addClass('catalog-part');
    $partsDiv.attr({'mfr': mfr, 'model': model});
    $partsDiv.prepend(jQuery('<img>', {src: imgURL}));

    //Write overlay div
    var $overlayDiv = jQuery("<div/>");
    $overlayDiv.addClass('overlay');
    var txt2 = jQuery("<p></p>").html(mfr + " " + partNum + "<br>" + orders + "Orders SAMPLE <br>" + price + " " + avail);
    $overlayDiv.prepend(txt2);

    //Assemble full catalog-par div 
    $partsDiv.append($overlayDiv);
    parent.append($partsDiv);

}

jQuery(document).ready(function ($) {
    readData(jQuery("#parts-content"));

    ///CODE FOR NAVIGATION
    $("#search-btn").on("click", function () {
        $('.catalog-part').show(); //on new search, start w/ all parts
        var selmfr = $('#dd-mfr').find(':selected').val();
        console.log("selected mfr " + selmfr); //this just for testing/debugging
        if (selmfr == "All") {
            //do nothing
        } else {
            $('.catalog-part').each(function () {
                if ($(this).attr('mfr').indexOf(selmfr) < 0) {
                    $(this).hide();
                } else {
                    $(this).show();
                }
            });
        }

        var selmodel = $('#dd-model').find(':selected').val();
        console.log("selected model " + selmodel); //this just for testing/debugging
        if (selmodel == "All") {
            //do nothing
        } else {
            $('.catalog-part').each(function () {
                if ($(this).attr('model').indexOf(selmodel) < 0) {
                    $(this).hide();
                } else {
                    //$(this).show();
                }
            });
        }
    });


});