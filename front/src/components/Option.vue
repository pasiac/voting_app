<template>
  <div class="options" >
    <p class="option" v-bind:class="{ correct: option.is_correct }">{{ option.title }}</p>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "Option",
  props: ['option_url'],
  data () {
    return {
      option: {title: 'brak', is_correct: false}
    }
  },
  mounted() {
    this.getOption()
  },
  methods: {
    getOption() {
      axios({
        method: 'get',
        url: this.option_url,
        auth: {
          username: 'admin',
          password: 'admin'
        }
      }).then(response => this.option = response.data)
    },
  }
}

</script>

<style scoped>
  .correct {
    color: green;
  }
</style>