/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {

    const obj = {
        orig_value: init,
        curr_value: init,
        increment: function() {
            this.curr_value += 1;
            return this.curr_value;
        },
        decrement: function() {
            this.curr_value  -= 1;
            return this.curr_value;
        },
        reset: function() {
            this.curr_value = this.orig_value;
            return this.curr_value;
        }
    };
    return obj;
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */