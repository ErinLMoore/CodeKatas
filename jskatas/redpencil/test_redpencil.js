QUnit.test("discount must be at least 5% to start promo", function(assert) {
	var expected = true;
	var result = discount_not_too_low(1, .5);
	assert.equal(result, true);
	var expected = false;
	var result =  discount_not_too_low(1, .97);
	assert.equal(result, false);
});

QUnit.test("discount must be %30 or under to start promo", function(assert) {
	var expected = true;
	var result = discount_not_too_high(1, .5);
	assert.equal(result, true);
	var expected = false;
	var result = discount_not_too_high(1, .2);
	assert.equal(result, false);
});

QUnit.test("discount in right range", function(assert) {
	var expected = true
	var result = discount_in_right_range(1, .5);
	assert.equal(result, true);
	var expected = false;
	var result = discount_in_right_range(1, .97);
	assert.equal(result, false);
	var expected = false;
	var result = discount_in_right_range(1, .05);
	assert.equal(result, false);
});

QUnit.test("promo length 30 days or less", function(assert) {
	var expected = true
	var result = promo_length_valid(15);
	assert.equal(result, true);
	var expected = false
	var result = promo_length_valid(31);
	assert.equal(result, false);
});
