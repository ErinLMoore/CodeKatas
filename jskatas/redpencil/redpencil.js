function  discount_not_too_low(oldprice, newprice) {
  var result = ((oldprice*.95)>=newprice);
  return result;
}

function discount_not_too_high(oldprice, newprice){
  var result = ((oldprice*.30)<=newprice);
  return result;
}
