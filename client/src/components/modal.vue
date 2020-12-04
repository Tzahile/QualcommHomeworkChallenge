<template>
  <div>
    <div class="layer"></div>
    <div
      id="modal"
      class="modal"
      :class="modalType === 'delete' ? 'half-card' : 'full-card'"
    >
      <div class="card">
        <span>
          <font-awesome-icon
            @click="$emit('close')"
            class="icon float-right"
            icon="times"
            size="lg"
          ></font-awesome-icon>

          <div class="header">
            <template v-if="modalType == 'delete'"> Delete Version </template>
            <template v-else-if="modalType == 'edit'">
              <header>Edit Notes</header>
            </template>
            <template v-else-if="modalType == 'new'">
              <header>Create Version</header>
            </template>
          </div>
        </span>
        <div class="content">
          <div class="delete-content" v-if="modalType == 'delete'">
            Are you sure you want to delete version
            <b>{{ card.id }}</b>
            ?
          </div>
          <template v-else>
            <version-card
              :form="changeform"
              v-bind="card"
              :error="error"
              :editMode="modalType == 'edit'"
              :emptyMode="modalType == 'new'"
            ></version-card>
          </template>
        </div>
        <footer class="modal-footer">
          <button
            class="btn"
            :class="modalType === 'delete' ? 'error-back' : 'success-back'"
            @click="
              modalType === 'delete'
                ? $emit(modalType, card)
                : $emit(modalType, form)
            "
          >
            <template v-if="modalType == 'delete'">Delete</template>
            <template v-else-if="modalType == 'edit'">
              <header>Save</header>
            </template>
            <template v-else-if="modalType == 'new'"> Create </template>
          </button>
        </footer>

        <template v-if="modalType == 'new'"></template>
      </div>
    </div>
  </div>
</template>

<script>
import versionCard from "@/components/versionCard.vue";

export default {
  components: {
    versionCard,
  },
  props: {
    show: Boolean,
    modalType: String,
    card: Object,
    editMode: Boolean,
    error: {
      type: Boolean,
      default: false,
    },
  },
  watch: {
    error(newValue) {
      console.log(newValue);
    },
  },
  data() {
    return {};
  },
  created() {
    /* eslint-disable */
    this.form = {};
    if (!this.card) {
      this.form.id = undefined;
      this.form.date = undefined;
      this.form.notes = undefined;
      this.form.author = undefined;
    } else {
      this.form.id = this.card.id;
    }
  },
  computed: {
    formId() {
      return this.form.id;
    },
  },
  methods: {
    changeform({ id, date, notes, author }) {
      if (id) this.form.id = id.target.value;
      if (date) this.form.date = date.target.value;
      if (notes && typeof notes.target.value === "string") {
        this.form.notes = notes.target.value;
      }
      if (author) this.form.author = author.target.value;
    },
  },
};
</script>

<style lang="scss">
.layer {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  opacity: 0.6;
  background-color: black;
  z-index: 1;
}
.modal {
  display: flex;
  flex-direction: column;
  background-color: white;
  opacity: 1;
  z-index: 3;
  position: fixed;
  left: 0;
  top: 0;
  width: 65%;
  margin-left: 20vw;
}

.full-card {
  min-height: 60%;
  margin-top: 7%;

  .action-btn {
    bottom: 5%;
    position: absolute;
  }
}
.half-card {
  height: 20%;
  margin-top: 20%;

  .action-btn {
    bottom: 10%;
  }
}
.action-btn {
  left: 85%;
}
.modal-footer {
  float: right;
  position: relative;
  height: 75px;
}
.float-right {
  float: right;
}
.header {
  padding: 4px 0px 10px;
  font-weight: 700;
  font-size: x-large;
  border-bottom: #ccc solid 1px;
}
.delete-content {
  padding-top: 15px;
}
.content {
  padding: 10px 0;

  .card {
    max-height: 50vh;
    overflow-x: auto;
    padding-bottom: 20px;
  }
}
</style>
