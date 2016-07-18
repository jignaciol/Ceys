var ceys = ceys || {}

ceys.views.clockView = Backbone.View.extend({

    template: _.template( ceys.utils.loadHtmlTemplate("clock") ) ,

    render: function() {
        this.$el.html("")
        this.$el.html(this.template(this.model.toJSON()))
    },

    initialize: function() {
        this.model.on('change', this.render, this)
        this.render()
    }

})
