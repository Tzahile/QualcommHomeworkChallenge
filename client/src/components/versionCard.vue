<template>
  <div class="card">
    <header class="card-header">
      <span :class="{ 'card-title': !emptyMode }">
        <template v-if="!emptyMode"> v{{ id }} </template>
        <template v-else>
          <div class="input-title">Version</div>
          <input @change="form({ id: $event })" class="input" type="text" />
          <div class="error-font" v-if="error">Invalid Value!</div>
        </template>
      </span>
      <span class="icons float-right" v-if="!editMode && !emptyMode">
        <font-awesome-icon
          class="icon"
          @click="$emit('edit')"
          icon="pencil-alt"
          size="lg"
        ></font-awesome-icon>
        <font-awesome-icon
          class="icon error-font"
          @click="$emit('delete')"
          icon="trash"
          size="lg"
        ></font-awesome-icon>
      </span>
    </header>
    <div class="card-date">
      <template v-if="!emptyMode">
        <b>{{ author }}</b> released this on {{ date }}
      </template>
      <template v-else>
        <div class="input-title">Author</div>
        <input @change="form({ author: $event })" class="input" type="text" />
      </template>
    </div>
    <div class="card-body">
      <div v-if="emptyMode" class="input-title">Notes</div>
      <textarea
        class="editArea"
        v-if="editMode || emptyMode"
        @change="form({ notes: $event })"
        v-text="editNotes"
      >
      </textarea>
      <vue-markdown :source="notes" :watches="[notes]" v-else> </vue-markdown>
    </div>
  </div>
</template>

<script>
import VueMarkdown from "vue-markdown";

export default {
  props: {
    editMode: {
      type: Boolean,
      default: false,
    },
    emptyMode: {
      type: Boolean,
      default: false,
    },
    id: {
      type: String,
      // required: true,
    },
    date: {
      type: String,
      // required: true,
    },
    notes: {
      type: String,
      // required: true,
    },
    author: {
      type: String,
      // required: true,
    },
    error: {
      type: Boolean,
      default: false,
    },
    form: Function,
  },
  watch: {
    error(newValue) {
      console.log(newValue);
    },
    notes(newValue) {
      console.log("Got new value!");
      console.log(newValue);
    },
  },
  data() {
    return {};
  },
  computed: {
    editNotes() {
      return this.notes || "";
    },
  },
  components: { VueMarkdown },
};
</script>

<style lang="scss">
.card {
  padding: 20px;
}
.card:hover {
  .icons {
    opacity: 1;
    visibility: visible;
  }
}
.card-header {
  padding: 10px;
  justify-content: space-between;
  /* background-color: grey; */
}
.card-title {
  font-size: xx-large;
}
.card-date {
  padding: 10px;
  /* background-color: green; */
}
.card-body {
  padding: 10px;
}
.icon {
  align-self: center;
  justify-self: end;
  transition: 0.2s background-color ease-out;
  background-color: transparent;
  height: 35px;
  cursor: pointer;
  padding-left: 5px;
  margin-left: 5px;
  padding-right: 5px;
  margin-right: 5px;
  border-radius: 100%;
}
.icon:hover {
  background: #eee;
}
.icons {
  visibility: hidden;
  opacity: 0;
  transition: visibility 0.3s linear, opacity 0.3s linear;
  padding-top: 1px;
}
.error-font {
  color: #ff5252;
}
.error-back {
  color: white;
  background-color: #ff5252;
}
.success-font {
  color: #1867c0;
}
.success-back {
  color: white;
  background-color: #1867c0;
}
.input-title {
  font-weight: 600;
}
.input {
  height: 25px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: large;
}
.input:focus {
  outline-width: 0;
}
.editArea {
  width: -webkit-fill-available;
  max-width: -webkit-fill-available;
  height: 290px;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-size: medium;
}

.editArea:focus {
  outline-width: 0;
}
</style>
