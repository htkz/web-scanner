transToSearch = () => {
    $('#result').hide('400', () => {
        $('#search').show('400');
    });
}

transToResult = () => {
    $('#search').hide('400', () => {
        $('#result').show('400');
    });
}
