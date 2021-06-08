<template>
  <ul class="options">
    <li
        v-for="option in options" :key="option.id"
        :class="[
              {correct : option.is_correct & clickedName === option.title},
              {wrong : !option.is_correct & clickedName === option.title}
            ]"
        @click="handleClick(option)">
      {{ option.title }}
    </li>
  </ul>
</template>

<script>
import axios from 'axios';

export default {
  name: "Options",
  props: ['options_url'],
  data() {
    return {
      options: [],
      isClicked: false,
      clickedName: ''
    }
  },
  mounted() {
    this.getOptions()
  },
  methods: {
    getOptions() {
      // Fix to some axios multi request function
      this.options_url.forEach(option_url => {
        axios({
          method: 'get',
          url: option_url,
          auth: {
            username: 'admin',
            password: 'admin'
          }
        }).then(response => this.options.push(response.data))
      })
    },
    handleClick(option) {
      if (!this.isClicked) {
        this.clickedName = option.title;
        this.isClicked = true;
      }
    }
  }
}

</script>

<style scoped>
  .correct {
    background-color: green;
  }

  .wrong {
    background-color: red;
  }
</style>