Java.perform(function () {
    const LicenseUtils = Java.use('com.ethan.v2x.utils.LicenseUtils')
    LicenseUtils.licenseDecode.implementation = function (a, b) {
        console.log('a value:' + a);
        console.log('b value:' + b);
        return this.licenseDecode(a, b)
    };
});


