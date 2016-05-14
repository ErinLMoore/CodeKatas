todays_date = new Date()

QUnit.test("discount must be at least 5% to start promo", function(assert) {
	var expected = true;
	var result = discount_not_too_low(1, .5);
	assert.equal(result, expected);
	var expected = false;
	var result =  discount_not_too_low(1, .97);
	assert.equal(result, expected);
});

QUnit.test("discount must be %30 or under to start promo", function(assert) {
	var expected = true;
	var result = discount_not_too_high(1, .5);
	assert.equal(result, expected);
	var expected = false;
	var result = discount_not_too_high(1, .2);
	assert.equal(result, expected);
});

QUnit.test("discount in right range", function(assert) {
	var expected = true
	var result = discount_in_right_range(1, .5);
	assert.equal(result, expected);
	var expected = false;
	var result = discount_in_right_range(1, .97);
	assert.equal(result, expected);
	var expected = false;
	var result = discount_in_right_range(1, .05);
	assert.equal(result, expected);
});

QUnit.test("price_stable_for_30_days", function(assert) {
	past_date = new Date()
	past_date.setDate( todays_date.getDate()-40)
	var expected = true;
	var result = price_stable_long_enough(past_date);
	assert.equal(result, expected);

	past_date = new Date()
	past_date.setDate( todays_date.getDate()-2)
	var expected = false;
	var result = price_stable_long_enough(past_date );
	assert.equal(result, expected);
});


QUnit.test("promo length 30 days or less", function(assert) {
	future_date = new Date();
	future_date.setDate =  todays_date.getDate()+15;
	var expected = true
	var result = promo_length_valid(future_date);
assert.equal(result, expected);

 future_date = new Date(2016,6,30);
 //future_date.setTime=  todays_date.getTime +(32*(24*60*60*1000)) ;
	var expected = false;
	var result = promo_length_valid(future_date);
assert.equal(result, expected);
});

QUnit.test("validate_promo_end_to_end", function(assert) {
	qitem = new Item(new Date(2016,2,1), 1)
	qpromo = new Promo(new Date(2016,4,30), .75, qitem)
	var expected = true;
	var result = validate_promo(qpromo);
	assert.equal(result, expected);

	qitem = new Item(new Date(2016,4,1), 1)
	qpromo = new Promo(new Date(2016,4,30), .95, qitem)
	var expected = false;
	var result = validate_promo(qpromo);
	assert.equal(result, expected);
});
