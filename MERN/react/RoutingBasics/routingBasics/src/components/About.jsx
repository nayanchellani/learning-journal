import React from "react";

export default function About() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 via-white to-blue-100 p-6">
      <div className="max-w-2xl w-full bg-white rounded-2xl shadow-xl p-8 border border-gray-200 transition-all duration-300 hover:shadow-2xl">
        
        {/* Heading */}
        <h1 className="text-4xl font-extrabold text-gray-800 text-center mb-4">
          About Us
        </h1>
        
        {/* Subtitle */}
        <p className="text-gray-600 text-lg text-center mb-6">
          Learn more about our journey and what makes us unique 🚀
        </p>

        {/* Content */}
        <div className="space-y-4 text-gray-700 text-base leading-relaxed">
          <p>
            Welcome to our website! We are passionate about building amazing web
            applications and delivering high-quality solutions. Our goal is to
            make learning modern technologies easy and fun.
          </p>
          <p>
            This project is part of our <span className="font-semibold text-blue-600">React Learning Journey</span>.
            We're exploring React Router, hooks, and component-based UI design
            to create smooth and interactive experiences.
          </p>
          <p>
            If you're excited about React, JavaScript, and modern web
            development, you’re in the right place! 🎯
          </p>
        </div>

        {/* Call-to-Action Button */}
        <div className="mt-6 flex justify-center">
          <button className="px-6 py-3 bg-blue-600 text-white rounded-xl shadow-md hover:bg-blue-700 hover:shadow-lg transition-all duration-300">
            Learn More
          </button>
        </div>
      </div>
    </div>
  );
}
