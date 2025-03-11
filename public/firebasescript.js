// Import the functions you need from the SDKs you need
import firebase from 'firebase/app';
import 'firebase/firestore';
import 'firebase/auth';
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBaOw6KBG26rLLeB1gRL6kGEfh8vrIi5OE",
  authDomain: "hclw-c41cc.firebaseapp.com",
  projectId: "hclw-c41cc",
  storageBucket: "hclw-c41cc.firebasestorage.app",
  messagingSenderId: "614899622239",
  appId: "1:614899622239:web:cb76e605725700db2256ea",
  measurementId: "G-C93YVSG1YX"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

firebase.initializeApp(firebaseConfig);

export const db = firebase.firestore();
export const auth = firebase.auth()
export default firebase;