
max_promo_length = 30
min_discount_percent = .05
max_discount_percent = .3
price_stability_length_required = 30

function discount_in_right_range(oldprice, newprice){
  return discount_not_too_low(oldprice, newprice)&&
          discount_not_too_high(oldprice, newprice);
}

function promo_length_valid(startdate,enddate){
  return ((enddate-startdate) <=max_promo_length);
}

function price_stable_long_enough(lastchangedate, newchangedate){
    return (newchangedate-lastchangedate >=price_stability_length_required);
}

function  discount_not_too_low(oldprice, newprice) {
  var result = ((oldprice-newprice )>=oldprice*min_discount_percent);
  return result;
}

function discount_not_too_high(oldprice, newprice){
  var result = ((oldprice*max_discount_percent)<=newprice);
  return result;
}
