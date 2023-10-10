// The MIT License (MIT)
//
// Copyright 2023 RT Corporation <support@rt-net.jp>
//
// Permission is hereby granted, free of charge, to any person obtaining a copy of
// this software and associated documentation files (the "Software"), to deal in
// the Software without restriction, including without limitation the rights to
// use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
// the Software, and to permit persons to whom the Software is furnished to do so,
// subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
// FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
// COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
// IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
// CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


#ifndef RASPIMOUSE_FAKE__VISIBILITY_CONTROL_H_
#define RASPIMOUSE_FAKE__VISIBILITY_CONTROL_H_

#ifdef __cplusplus
extern "C"
{
#endif

#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define RASPIMOUSE_FAKE_EXPORT __attribute__ ((dllexport))
    #define RASPIMOUSE_FAKE_IMPORT __attribute__ ((dllimport))
  #else
    #define RASPIMOUSE_FAKE_EXPORT __declspec(dllexport)
    #define RASPIMOUSE_FAKE_IMPORT __declspec(dllimport)
  #endif
  #ifdef RASPIMOUSE_FAKE_BUILDING_DLL
    #define RASPIMOUSE_FAKE_PUBLIC RASPIMOUSE_FAKE_EXPORT
  #else
    #define RASPIMOUSE_FAKE_PUBLIC RASPIMOUSE_FAKE_IMPORT
  #endif
  #define RASPIMOUSE_FAKE_PUBLIC_TYPE RASPIMOUSE_FAKE_PUBLIC
  #define RASPIMOUSE_FAKE_LOCAL
#else
  #define RASPIMOUSE_FAKE_EXPORT __attribute__ ((visibility("default")))
  #define RASPIMOUSE_FAKE_IMPORT
  #if __GNUC__ >= 4
    #define RASPIMOUSE_FAKE_PUBLIC __attribute__ ((visibility("default")))
    #define RASPIMOUSE_FAKE_LOCAL  __attribute__ ((visibility("hidden")))
  #else
    #define RASPIMOUSE_FAKE_PUBLIC
    #define RASPIMOUSE_FAKE_LOCAL
  #endif
  #define RASPIMOUSE_FAKE_PUBLIC_TYPE
#endif

#ifdef __cplusplus
}
#endif

#endif  // RASPIMOUSE_FAKE__VISIBILITY_CONTROL_H_
