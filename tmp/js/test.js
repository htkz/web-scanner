const data = `
[
    {
        "demo.aisec.cn":
            [
                {
                    "demo":
                    [
                        {
                            "aisec":
                            [
                                "html_link.php",
                                "js_link.php",
                                "post_link.php",
                                "click_link.php"
                            ]
                        }
                    ]
                }
            ]
    }
]`

console.log(JSON.parse(data));


$('.structure p').each(function(index, el) {
    let level = $(el).attr('class').split('level')[1];
    let offset = level * 10;
    $(this).css('margin-left', `${offset}px`);

});
