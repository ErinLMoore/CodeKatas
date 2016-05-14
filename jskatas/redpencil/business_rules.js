
max_promo_length = 30
min_discount_percent = .05
max_discount_percent = .3
price_stability_length_required = 30
date_offset = (24*60*60*1000) * price_stability_length_required
todays_date = new Date()

function validate_promo(promo){
  this.item = promo.item
  var is_valid =discount_in_right_range(this.item.currentprice, promo.newprice) &&
    promo_length_valid(promo.enddate)&&
    price_stable_long_enough(this.item.dateoflastchange);
    this.item.underredpencil = is_valid
    return is_valid
}

function discount_in_right_range(oldprice, newprice){
  return discount_not_too_low(oldprice, newprice)&&
          discount_not_too_high(oldprice, newprice);
}

function promo_length_valid(enddate){
  diff = Math.abs(todays_date-enddate)
  return (diff <=date_offset);
}

function price_stable_long_enough(dateoflastchange){
    today_ms = todays_date.getTime();
    last_change_ms = dateoflastchange.getTime();
    var diff = Math.abs(today_ms-last_change_ms);
    console.log(diff);
    return (diff >=date_offset);
    //diff = Math.abs(todays_date-dateoflastchange)
    //return (diff >=date_offset);
}

function  discount_not_too_low(oldprice, newprice) {
  var result = ((oldprice-newprice )>=oldprice*min_discount_percent);
  return result;
}

function discount_not_too_high(oldprice, newprice){
  var result = ((oldprice*max_discount_percent)<=newprice);
  return result;
}
