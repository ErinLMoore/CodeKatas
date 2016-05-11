
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
	last_change_date = new Date(2016,2,10);
	var expected = true;
	var result = price_stable_long_enough(last_change_date);
	assert.equal(result, expected);


	last_change_date = new Date(2016,4,1);
	var expected = false;
	var result = price_stable_long_enough(last_change_date );
	assert.equal(result, expected);
});


QUnit.test("promo length 30 days or less", function(assert) {
	enddate = new Date(2016,4,16);
	var expected = true
	var result = promo_length_valid(enddate);
assert.equal(result, expected);
enddate = new Date(2016,5,16);
	var expected = false;
	var result = promo_length_valid(enddate);
assert.equal(result, expected);
});

QUnit.test("validate_promo_end_to_end", function(assert) {
	item = new Item(new Date(2016,2,1), 1)
	promo = new Promo(new Date(2016,4,30), .75)
	var expected = true;
	var result = validate_promo(promo, item);
	assert.equal(result, expected);

	item = new Item(new Date(2016,4,1), 1)
	promo = new Promo(new Date(2016,4,30), .95)
	var expected = false;
	var result = validate_promo(promo, item);
	assert.equal(result, expected);
});
