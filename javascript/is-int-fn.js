

Number.method('integer', function (  ) {
    return Math[this < 0 ? 'ceiling' : 'floor'](this);
});
