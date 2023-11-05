<template>
  <button
    class="btn-comp"
    :class="`${classes}${loading ? ' loading' : ''}${disabled ? 'cursor-not-allowed' : ''}`"
    :disabled="loading || disabled"
  >
    <div class="loader loader--small" :class="`loader--${loaderColor}`">
      <span />
      <span class="dot--second" />
      <span class="dot--third" />
    </div>
    <span class="content">
      <slot />
    </span>
  </button>
</template>

<script>
export default {
  name: "Button",
  props: {
    loading: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    classes: {
      type: String,
      default: "",
    },
    loaderColor: {
      type: String,
      default: "white",
    }
  },
};
</script>

<style>
  button.btn-comp {
    min-width: 6rem;
  }
  button.loading, button.cursor-not-allowed {
    cursor: not-allowed;
  }
  button.loading {
    position: relative;
  }
  button.loading .content {
    opacity: 0;
  }
  button.loading .loader {
    position: absolute;
    left: 0;
    top: 50%;
    transform: translate(0, -50%);
    width: 100%;
  }
  button.loading .loader > * {
    display: inline-block;
    border-radius: 50%;
    animation: wave 1.3s linear infinite;
  }
  button.loading .loader > *.dot--second {
    animation-delay: -1.1s;
  }
  button.loading .loader > *.dot--third {
    animation-delay: -0.9s;
  }
  button.loading .loader--white > * {
    background: white;
  }
  button.loading .loader--gray > * {
    background: #bdbdbd;
  }
  button.loading .loader--red > * {
    background: #ed4c78;
  }
  button.loading .loader--blue > * {
    background: #304f95;
  }
  button.loading .loader--big > * {
    width: 2rem;
    height: 2rem;
  }
  button.loading .loader--big > *.dot--second,  button.loading .loader--big > *.dot--third {
    margin-left: 2.5rem;
  }
  button.loading .loader--regular > * {
    width: 1rem;
    height: 1rem;
  }
  button.loading .loader--regular > *.dot--second,  button.loading .loader--regular > *.dot--third {
    margin-left: 1.2rem;
  }
  button.loading .loader--small > * {
    width: 0.4rem;
    height: 0.4rem;
  }
  button.loading .loader--small > *.dot--second,  button.loading .loader--small > *.dot--third {
    margin-left: 0.2rem;
  }

  @keyframes wave {
    0%, 60%, 100% {
      transform: initial;
    }

    30% {
      transform: translateY(-.50rem);
    }
  }
</style>