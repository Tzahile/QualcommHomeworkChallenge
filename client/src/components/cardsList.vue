<template>
  <div>
    <div class="nav-bar">
      <span class="list-title">Changelog</span>
      <font-awesome-icon
        class="icon success-font"
        icon="plus"
        @click="OpenModal('new')"
        size="lg"
      ></font-awesome-icon>
    </div>
    <div class="main-list" v-if="CardsLoaded">
      <modal
        v-if="showModal"
        :editMode="modalEditMode"
        :card="modalCard"
        :modalType="modalType"
        :error="invalidId"
        @close="CloseModal"
        @delete="DeleteCard"
        @new="CreateCard"
        @edit="EditCard"
      >
      </modal>
      <template v-for="(card, index) in cards">
        <version-card
          @edit="OpenModal('edit', card)"
          @delete="OpenModal('delete', card)"
          :key="'card' + index"
          v-bind="card"
        ></version-card>
        <hr :key="'hr' + index" />
      </template>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import versionCard from "@/components/versionCard.vue";
import modal from "@/components/modal.vue";
import {
  UpdateVersion,
  DeleteVersion,
  CreateVersion,
} from "@/apis/versions.js";
export default {
  components: {
    versionCard,
    modal,
  },
  async created() {
    let result = await axios.get("/versions");
    this.cards = result.data.sort(SortByVersion);
  },
  data() {
    return {
      cards: undefined,
      invalidId: false,
      showModal: false,
      modalCard: undefined,
      modalType: undefined,
      modalEditMode: undefined,
    };
  },
  computed: {
    CardsLoaded() {
      return this.cards;
    },
  },
  methods: {
    GetDate() {
      const [month, day, year] = new Date().toLocaleDateString().split("/");
      return `${day}-${month}-${year}`;
    },
    OpenModal(operation, card) {
      if (operation === "new") {
        this.modalEditMode = true;
        this.modalCard = {
          id: undefined,
          date: undefined,
          notes: undefined,
          author: undefined,
        };
      }
      if (operation === "delete") this.modalCard = card;
      if (operation === "edit") {
        this.modalEditMode = true;
        this.modalCard = card;
      }
      this.modalType = operation;
      this.showModal = true;
    },
    CloseModal() {
      this.invalidId = false;
      this.showModal = false;
    },
    async CreateCard(card) {
      this.invalidId = false;
      if (!card.id || card.length == 0) {
        this.invalidId = true;
      } else {
        card.date = this.GetDate();
        try {
          await CreateVersion(card);
          this.cards.unshift(card);
          console.log(this.cards);
        } catch (error) {
          console.log(error);
        }
        this.CloseModal();
      }
    },
    async EditCard(card) {
      if (card.notes == undefined) return this.CloseModal();
      /* eslint-disable */
      debugger;
      const cards = this.cards;
      const cardIndex = this.GetCardIndex(card.id);
      // const newCard = {
      //   ...cards[cardIndex],
      //   notes: card.notes,
      // };
      try {
        await UpdateVersion(card);
        // this.cards.splice(cardIndex, 1, newCard);
        // cards[cardIndex].notes = card.notes;
        Vue.set(cards[cardIndex], "notes", card.notes);
        // Vue.cards;
      } catch (error) {
        console.log(error);
      }
      this.CloseModal();
    },
    async DeleteCard(card) {
      try {
        await DeleteVersion(card);
        this.$delete(this.cards, this.GetCardIndex(card.id));
        console.log(this.cards);
      } catch (error) {
        console.log(error);
      }
      this.CloseModal();
    },
    GetCardIndex(id) {
      return this.cards.indexOf(this.cards.filter((card) => card.id === id)[0]);
    },
  },
};

function SortByVersion(card1, card2) {
  const [major1, minor1, patch1] = card1.id.split(".");
  const [major2, minor2, patch2] = card2.id.split(".");
  if (major2 !== major1) return Number(major2) - Number(major1);
  if (minor2 !== minor1) return Number(minor2) - Number(minor1);
  if (patch2 !== patch1) return Number(patch2) - Number(patch1);
}
</script>

<style lang="scss">
.main-list {
  margin-top: 100px;
  border-left: solid thin #ccc;
  margin-left: 15%;
  margin-right: 15%;
}

.list-title {
  position: absolute;
  margin: 15px;
  font-weight: 600;
  font-size: x-large;
}

hr {
  background-color: #ccc;
  height: 1px;
  border: 0;
  margin-left: 10px;
  margin-right: 10px;
}

.nav-bar {
  display: inline-grid;
  z-index: 1;
  overflow: hidden;
  background-color: #fff;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 60px;

  box-shadow: grey 0px 2px 20px 2px;
}
</style>
