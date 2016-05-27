todays_date = new Date()
valid_promo_date = new Date()
valid_promo_date.setDate( todays_date.getDate()+15);
invalid_promo_date = new Date()
invalid_promo_date.setDate( todays_date.getDate()+35);


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

QUnit.test("promo length 30 days or less", function(assert) {
	future_date = new Date();
	future_date.setDate =  todays_date.getDate()+15;
	var expected = true
	var result = promo_length_valid(valid_promo_date);
assert.equal(result, expected);

 future_date = new Date(2016,6,30);
 future_date.setDate =  todays_date.getDate()+35;
	var expected = false;
	var result = promo_length_valid(invalid_promo_date);
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


QUnit.test("validate_promo_end_to_end", function(assert) {
	qitem = new Item(new Date(todays_date.getDate()-45), 1)
	qpromo = new Promo(valid_promo_date, .75)
	var expected = true;
	var result = validate_promo(qpromo, qitem);
	assert.equal(result, expected);

	qitem = new Item(new Date(todays_date.getDate()-15), 1)
	qpromo = new Promo(invalid_promo_date, .95)
	var expected = false;
	var result = validate_promo(qpromo, qitem);
	assert.equal(result, expected);
});

QUnit.test("store takes in promo and adds it", function(assert){
	qstore = new Store()
	qpromo = new Promo(new Date(2016,4,30), .75)
	qstore.add_promo(qpromo, qstore.items[0]);
	var expected = 1;
	var result = qstore.promos.length;
	assert.equal(result, expected);

	qstore = new Store()
	qpromo = new Promo(new Date(2016,6,30), .95)
	qstore.add_promo(qpromo, qstore.items[0]);
	var expected = 0;
	var result = qstore.promos.length;
	assert.equal(result, expected);
});

QUnit.test("promo changes item to under red pencil", function(assert){
	qstore = new Store()
	qpromo = new Promo(valid_promo_date, .75)
	qstore.add_promo(qpromo, qstore.items[0]);
	var expected = true;
	var result = qstore.items[0].underredpencil;
	assert.equal(result, expected);
});

QUnit.test("if item under red pencil do nothing", function(assert){
	qstore = new Store()
	qpromo = new Promo(valid_promo_date, .75)
	qstore.items[0].underredpencil = true;
	qstore.add_promo(qpromo, qstore.items[0]);
	var expected = 0;
	var result = qstore.promos.length;
	assert.equal(result, expected);
});
