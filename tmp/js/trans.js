transToSearch = () => {
    $('#result').hide('400', () => {
        $('.search-wraper').show('400');
    });
}

transToResult = () => {
    $('.search-wraper').hide('400', () => {
        $('#result').show('400');
    });
}
